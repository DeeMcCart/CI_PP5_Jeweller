from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product
import time

# Create your views here.

def view_basket(request):
    """ A view that renders the bag contents page """

    return render(request, 'basket/basket.html')

def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """

    product = get_object_or_404(Product, pk=item_id)
    print(f'Product found')
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        print(f'Product {product.name} added to basket')
        time.sleep(1)
        messages.success(request, f'Added another {product.name} to your basket')
        time.sleep(1)
    else:
        basket[item_id] = quantity
        print(f'Product {product.name} added to basket')
        messages.success(request, f'Added {product.name} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    print(f"retrieved product ", product, " to adjust basket")
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(request, f'{product.name} quantity updated to {quantity}')

    else:
        basket.pop(item_id)
        messages.success(request, f'{product.name} removed from your basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """Remove the item from the shopping basket"""

    try:
        size = None
        basket = request.session.get('basket', {})
        product = get_object_or_404(Product, pk=item_id)

        basket.pop(item_id)
        messages.success(request, f'{product.name} removed from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)    
        messages.error(request, f'Unable to remove {product.name} from your basket')
