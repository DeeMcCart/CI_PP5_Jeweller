from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile

import json
import time
import stripe


class StripeWH_Handler:
    """Handle Stripe webhooks"""
    """ These webhooks are 'signals' sent from Stripe to a specified URL
        This tells our app that something is happening in Stripe and prevents
        an orphaned Stripe transaction (payment without an associated order)
    """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email
        # cc_email = settings.DEFAULT_CC_EMAIL
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        # send_email extended to include CC to shop's email address
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email],
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        # print out the payment intent coming from Stripe
        print(intent)

        pid = intent.id
        # DMcC 06/02/24 Changed 'bag' to 'basket' in next line:
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
                        intent.latest_charge)

        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        # Clean data in the shipping details, distinguish between Stripe
        # blank string and null value we want to store in our database
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number1 = shipping_details.phone
                profile.save()

        # assume the order doesnt yet exist
        order_exists = False
        attempt = 1
        # note that we are taking 5 attempts to check if the order exists
        # just because there could be a delay in asynch processing
        while attempt <= 5:
            # check if the order exists already
            # (based on exact match to the order details....)
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        # we expect that the order will already have been created
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: '
                        + 'Verified order already in database',
                status=200)
        # but if not then the webhook handler will cause it to be created
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                # DMcC 21/02/24:  Add logic to include project-specific fields
                # in order line item build so that webhook order lines follow
                # the same logic as 'mainstream' order lines => line_number,
                # sku, unit price, category
                # Order line numbr to start at 10 and increment by 10
                current_line_number = 10
                for item_id, item_data in json.loads(basket).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            # assign line number
                            line_number=current_line_number,
                            product=product,
                            sku=product.sku,
                            category=product.category,
                            quantity=item_data,
                            product_size='',
                            price=product.price,
                            lineitem_total=item_data
                        )
                        order_line_item.save()
                        current_line_number += 10
                    elif (isinstance(item_data, dict) and
                          "items_by_size" in item_data and
                          isinstance(item_data["items_by_size"], dict)):
                        for size, quantity in (item_data['items_by_size'].
                                               items()):
                            order_line_item = OrderLineItem(
                                order=order,
                                line_number=current_line_number,
                                product=product,
                                sku=product.sku,
                                category=product.category,
                                quantity=quantity,
                                product_size=size,
                                price=product.price,
                                lineitem_total=item_data,
                            )
                            order_line_item.save()
                            current_line_number += 10
                    elif (isinstance(item_data, dict) and
                          ("engrave_text" in item_data and
                          isinstance(item_data["engrave_text"], dict))):
                        for engrave_text, quantity in (
                                                    item_data['engrave_text'].
                                                    items()):
                            order_line_item = OrderLineItem(
                                order=order,
                                line_number=current_line_number,
                                product=product,
                                sku=product.sku,
                                product_size='',
                                category=product.category,
                                quantity=quantity,
                                # DMcC 01/03/24 add a value for can_be_engraved
                                can_be_engraved=True,
                                engrave_text=engrave_text,
                                price=product.price,
                                lineitem_total=item_data,
                                )
                            order_line_item.save()
                            current_line_number += 10
                            # end for

            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: '
                    + 'Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
