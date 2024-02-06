from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from basket.contexts import basket_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    # To be used before we call the confor card payent method in stripe js
    # We will mae a post request to this view, giving it the client secret
    # from the payment intent, which we can parse to extract intent ID (pid) 
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            # NB save_info reflects the user's choice to save the address info
            'save_info': request.POST.get('save_info'),
            'username': request.user,
            # DMcC 06/02/24 Add field 'description' here as placeholder for order #
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
            order.strip_pid= pid
            order.original_basket = json.dumps(basket)
            order.save()
            # DMcC 06/02/24:  Current line number starts at 10
            current_line_number=10
            for item_id, item_data in basket.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            # DMcC 06/02/24 line should be an increment of existing line #s
                            line_number=current_line_number, 
                            product=product,
                            quantity=item_data,
                            # DMcC 06/02/24 added line item price and total to model
                            price = product.price,
                            lineitem_total = item_data,
                            )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                line_number=current_line_number, 
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                    current_line_number+=10
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your basket wasn't found in our database. "
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
        # DMcC attempt to overcome issue with grand total not being saved to order 
        
        order.save()

        # save the user's info
        if save_info:
            # save the order information into default fields
            # DMcC 06/02/24 May need to re-look at the below as wish to choose which delivery address this saves to for the user
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
            print(f'Attempting to update default delivery adddress for customer profile')
            if user_profile_form.is_valid():
                user_profile_form.save()


    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}, total value {order.order_total}. A confirmation \
        email will be sent to {order.email}.')

    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)