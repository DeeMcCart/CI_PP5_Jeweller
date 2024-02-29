from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from basket.contexts import basket_contents
from profiles.views import profile_detail

import stripe
import json


@require_POST
def cache_checkout_data(request):
    # To be used before we call the confirm card payent method in stripe js
    # We will make a post request to this view, giving it the client secret
    # from the payment intent, which we can parse to extract intent ID (pid)
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            # NB save_info reflects the user's choice to save the address info
            'save_info': request.POST.get('save_info'),
            'username': request.user,
            # DMcC 06/02/24 Add field 'description' as placeholder for order #
            'description': 99999,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        ''' successful payment should trigger creation of an order '''
        basket = request.session.get('basket', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'delivery_method': request.POST['delivery_method'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            # parse out the payment id from Stripe
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_basket = json.dumps(basket)
            order.save()
            # DMcC 06/02/24:  Current line number starts at 10
            # Note additional fields added for Jeweller:
            # line_number, sku, category, size, total
            current_line_number = 10
            for item_id, item_data in basket.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            # DMcC 06/02/24 line#: increment of existg line #s
                            line_number=current_line_number,
                            product=product,
                            sku=product.sku,
                            category=product.category,
                            quantity=item_data,
                            product_size='Not set',
                            price=product.price,
                            lineitem_total=item_data,
                            )
                        order_line_item.save()
                        current_line_number += 10
                    elif isinstance(item_data, dict) and ("items_by_size" in item_data and isinstance(item_data["items_by_size"], dict)):
                        for size, quantity in item_data['items_by_size'].items():
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
                    elif isinstance(item_data, dict) and ("engrave_text" in item_data and isinstance(item_data["engrave_text"], dict)):
                        for engrave_text, quantity in item_data['engrave_text'].items():
                            order_line_item = OrderLineItem(
                            order=order,
                            line_number=current_line_number,
                            product=product,
                            sku=product.sku,
                            product_size='Not set',
                            category=product.category,
                            quantity=quantity,
                            engrave_text = engrave_text,
                            price=product.price,
                            lineitem_total=item_data,
                            )
                            order_line_item.save()
                            current_line_number += 10
                            # end for 
                    
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your basket wasn't found. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_basket'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, "There's nothing in your basket at the moment")
            return redirect(reverse('products'))

    current_basket = basket_contents(request)
    total = current_basket['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    # DMcC 07/02/24 copy delivery address from user to order (if exists)
    # DMcC 07/02/24 Needs more work to distinguish between ship and BILL addr
    # But lets assume BILL address for now.  Ref = Profile App Part 8
    if request.user.is_authenticated:
        try:
            bill_address = None
            profile = UserProfile.objects.get(user=request.user)
            if profile:
                addresses = profile.user_address.filter(address_type="BILL")
                if addresses:
                    bill_address = addresses[0]
            if bill_address:
                print(f'Found billing address ', {bill_address})
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.phone_number1,
                    'delivery_method': 'REGPOST',
                    'street_address1': bill_address.address1,
                    'street_address2': bill_address.address2,
                    'town_or_city': bill_address.town_or_city,
                    'county': bill_address.county,
                    'postcode': bill_address.postcode,
                    'country': bill_address.country,
                    })
            else:
                order_form = OrderForm()
        except UserProfile.DoesNotExist:
            order_form = OrderForm()
    else:
        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    if not stripe_secret_key:
        messages.warning(request, 'Stripe secret key is missing. \
            Where the heck is this supposed to be set in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # save the user's info
        if save_info:
            # save the order information into default fields
            # DMcC 06/02/24 May need to re-look at the below as wish to
            # choose which delivery address this saves to for the user
            # DMcC 07/02/24 Think this needs to save to the default
            # shipping address for the user?  Actually, think need to
            # look more
            # closely at the checkout process and determine where the
            # shipping and billing addresses are being asssigned
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_streeet_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            print('Updating default delivery adddress for user profile')
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order is {order_number}, total value {order.order_total}. \
         A confirmation email will be sent to {order.email}.')

    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)


def maint_orders(request):
    """ This is a sysadmin view to show all orders,
    and allow the sysadmin to edit/delete """
    print('In view maint_orders')
    orders = Order.objects.all()

    # sort by SKU in order asc/desc
    orders = orders.order_by('-order_number')
    context = {
        'orders': orders,
    }

    return render(request, 'checkout/maint_orders.html', context)

def order_late(request, order_id):
    """ determine if an order is late in shipping """
    """ based on order status and planned_ship_date """
    """ DMcC 14/02/24 Moved from Models as constantly recalculating"""
    now = timezone.now()
    order_late = False
    order=get_object_or_404(Order, pk=order_id)
    print(f'order.planned_ship_date', order.planned_ship_date)
    print(f'now', {now})
    if ((self.order_status in ['ORDERED', 'PACKED'])
        and (order.planned_ship_date < now)):
        order_late = True
    print(f'Order ', {self.order_number}, ' is ', {order_late}, ' late')
    return order_late

def send_update_email(request, order_id):
    """Send the user a confirmation email"""
    order=get_object_or_404(Order, pk=order_id)
    cust_email = order.email
    cc_email = settings.DEFAULT_CC_EMAIL
    subject = render_to_string(
        'checkout/confirmation_emails/update_email_subject.txt',
        {'order': order})
    body = render_to_string(
        'checkout/confirmation_emails/update_email_body.txt',
        {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

    # send_email extended to include CC to shop's email address
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email],
    )
    return True

def order_lines_text(request, order_id):
    """ Return a text string with order details """
    order = get_object_or_404(Order, order_number=order_number)
    stringy=""
    for item in order.lineitems.all:
        line_string = (f(item.product.name, " Size ", item.product_size|upper, " ", item.quantity, "@", item.product.price)) 
        string += line_string
        endwith
    endfor
    print(f" Order details string is ", stringy)
    return stringy

def next_status(request, order_id):
    """ Next status varies depending on delivery method:
    For COLLECT orders:
    Status ORDERED -> PACKED -> RECEIVED
    For REGPOST orders:
    Status ORDERED -> PACKED -> SHIPPED -> RECEIVED
    """
    order = get_object_or_404(Order, pk=order_id)
    current_status = order.order_status
    next_status = 'CLOSED'
    print(f'Order ', order.order_number, ' current status is ', current_status)
    if (current_status == 'ORDERED'):
       next_status = 'PACKED'
    elif ((current_status == 'PACKED')
          and (order.delivery_method == 'COLLECT')):
        next_status = 'RECEIVED'
    elif (current_status == 'PACKED'):
        next_status = 'SHIPPED'
    elif (current_status == 'SHIPPED'):
        next_status = 'RECEIVED'
    

    order.order_status=next_status
    order.save()
    messages.success(request, f' Order {order.order_number}'
                     + f' updated to status:{order.order_status}')
    
    # now send a message to the customer to tell them the order status has changed.
    send_update_email(request, order.id)
    
    # need to think about the ability to move through several stages at once, only really want one email
    # also need to gather tracker # for shipped items
    # What do we redisplay afterards?  The whole maintenance screen?
    # Should this be paginated?
    #  
    orders = Order.objects.all()

    # sort by SKU in order asc/desc
    orders = orders.order_by('-order_number')
    context = {
        'orders': orders,
    }

    return render(request, 'checkout/maint_orders.html', context)
