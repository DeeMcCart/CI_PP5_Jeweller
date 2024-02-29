from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):
    """ Create and maintain the basket contents
    """
    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for item_id, item_data in basket.items():
        if isinstance(item_data, int):
            # Product is not sized or engraved
            print('Item ','has item_data', item_data)
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            basket_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'price': product.price,
                'lineitem_total': item_data * product.price,
            })
        elif  isinstance(item_data, dict) and ("items_by_size" in item_data and isinstance(item_data["items_by_size"], dict)):
            # Product is sized
            print(f'Item data is ', item_data)
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                basket_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                    'price': product.price,
                    'lineitem_total': quantity * product.price,
                })
        elif  isinstance(item_data, dict) and ("engrave_text" in item_data and isinstance(item_data["engrave_text"], dict)):
            # Product is sized
            print(f'Item data is ', item_data)
            product = get_object_or_404(Product, pk=item_id)
            for engrave_text, quantity in item_data['engrave_text'].items():
                total += quantity * product.price
                product_count += quantity
                basket_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'engrave_text': engrave_text,
                    'price': product.price,
                    'lineitem_total': quantity * product.price,
                })
        
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
     
    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
