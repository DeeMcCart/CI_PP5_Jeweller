from django.shortcuts import (render, redirect, reverse, HttpResponse,
                              get_object_or_404)
from django.contrib import messages
from products.models import Product
# Create your views here.


def view_basket(request):
    """ A view that renders the basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    engrave_text = None
    if 'engrave_text' in request.POST:
        engrave_text = request.POST['engrave_text']
        print('In add_to_basket: Engrave text is  ', engrave_text)

    if 'product_size' in request.POST:
        size = request.POST['product_size'].strip()
        print('in add_to_basket: Requested product size is ', size)

    basket = request.session.get('basket', {})

    # if product already in basket, increment quantity if not sized
    # (rings to be sized will need to be stored on separate lines)
    if size:
        # update to datavalue['items_by_size'] within basket[item]
        if item_id in list(basket.keys()):
            if size in basket[item_id]['items_by_size'].keys():
                basket[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()}'
                                 + f'{product.name} quantity to '
                                 + f'{basket[item_id]["items_by_size"][size]}')
            else:
                basket[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} '
                                 + f'{product.name} to basket')
        else:
            basket[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} '
                             + f'{product.name} to basket')
    elif engrave_text:
        # update to datavalue['engrave_text'] within basket[item]
        if item_id in list(basket.keys()):
            if engrave_text in basket[item_id]['engrave_text'].keys():
                basket[item_id]['engrave_text'][engrave_text] += quantity
                new_quantity = basket[item_id]["engrave_text"][engrave_text]
                messages.success(request, f'Updated {product.name}, '
                                 + f'{engrave_text}, quantity to '
                                 + f'{new_quantity}')
            else:
                basket[item_id]['engrave_text'][engrave_text] = quantity
                messages.success(request, f'Added engraving {product.name},'
                                 + f' {engrave_text} to to your basket')
        else:
            basket[item_id] = {'engrave_text': {engrave_text: quantity}}
            messages.success(request, f'Added {product.name}, {engrave_text}'
                             + ' to to your basket')
    else:
        # update to basket[item].quantity
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity '
                             + f'to {basket[item_id]}')
        else:
            basket[item_id] = quantity
            messages.success(request, f'Added {product.name} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    engrave_text = None

    # DMcC 22/02/24 Reinstated size check for basket issuenum 84
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    elif 'engrave_text' in request.POST:
        engrave_text = request.POST['engrave_text']

    basket = request.session.get('basket', {})

    if size:
        if quantity > 0:
            basket[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} '
                             + f'{product.name} quantity to '
                             + f'{basket[item_id]["items_by_size"][size]}')
        else:
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
            messages.success(request, f'Removed size {size.upper()}'
                             + f'{product.name} from your basket')
    elif engrave_text:
        if quantity > 0:
            basket[item_id]['engrave_text'][engrave_text] = quantity
            messages.success(request, f'Updated  {product.name}, '
                             + f'{engrave_text} quantity to '
                             + f'{quantity}')
        else:
            del basket[item_id]['engrave_text'][engrave_text]
            if not basket[item_id]['engrave_text']:
                basket.pop(item_id)
            messages.success(request, f'Removed item {product.name},'
                             + f'{engrave_text} from basket')
    else:
        if quantity > 0:
            basket[item_id] = quantity
            messages.success(request, f'{product.name} qty '
                             + f'updated to {quantity}')
        else:
            basket.pop(item_id)
            messages.success(request, f'{product.name} removed from basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """Remove the item from the shopping basket"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        engrave_text = None

        if 'product_size' in request.POST:
            size = request.POST['product_size']
        elif 'engrave_text' in request.POST:
            engrave_text = request.POST['engrave_text']

        basket = request.session.get('basket', {})

        if size:
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
            messages.success(request, f'Removed size {size.upper()},'
                             + f'{product.name}, from basket')
        elif engrave_text:
            del basket[item_id]['engrave_text'][engrave_text]
            if not basket[item_id]['engrave_text']:
                basket.pop(item_id)
            messages.success(request, 'Removed size engravable item,'
                             + f'{product.name}, {engrave_text} from basket')
        else:
            basket.pop(item_id)
            messages.success(request, f'{product.name} removed from basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        print('Error', e)
        return HttpResponse(status=500)
        messages.error(request, f'Unable to remove {product.name} from basket')
