from django.db import models
from products.models import Product
from profiles.models import UserProfile
from django.conf import settings
from django.db.models import Sum, Max
from django.utils import timezone
from datetime import timedelta
from django_countries.fields import CountryField
import datetime

ORDER_STATUS_CHOICES = [
    ('ORDERED', 'Ordered'),
    ('PACKED', 'Packed'),
    ('SHIPPED', 'Shipped'),
    ('RECEIVED', 'Received'),
]

RING_SIZE_CHOICES = [
    ('H', 'Ring size H'),
    ('I', 'Ring size I'),
    ('J', 'Ring size J'),
    ('K', 'Ring size K'),
    ('L', 'Ring size L'),
    ('M', 'Ring size M'),
    ('N', 'Ring size N'),
    ('O', 'Ring size O'),
    ('P', 'Ring size P'),
    ('Q', 'Ring size Q'),
    ('R', 'Ring size R'),
    ('S', 'Ring size S'),
    ('', 'Not set'),
]

DELIVERY_METHODS = [
    ('REGPOST', 'RegisteredPost'),
    ('COLLECT', 'Click & Collect'),
]


# Create your models here.
class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    # note * is used on Country to indicate it is a required field
    country = CountryField(blank_label='Country *', default='IE',
                           null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    planned_ship_date = models.DateField(default=datetime.
                                         datetime(2024, 2, 28, 0, 0, 0))
    delivery_method = models.CharField(max_length=7, choices=DELIVERY_METHODS,
                                       default='REGPOST')
    delivery_track = models.CharField(max_length=13, null=True, blank=True)
    order_status = models.CharField(max_length=10, choices=ORDER_STATUS_CHOICES,
                                    default='ORDERED')
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    original_basket = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False,
                                  blank=False, default='')

    def _generate_order_number(self):
        """
        Generate a next number for the order based on determining the last
        order number written to file, and using it
        Else, if no orders on table, use settings.FIRST_ORDER_NUMBER
        """
        if (Order.objects.all().order_by('order_number').last()):
            max_order_number = Order.objects.all().order_by('order_number').last().order_number
            next_order_number = int(max_order_number) + 1
        else:
            next_order_number = settings.FIRST_ORDER_NUMBER
            settings.FIRST_ORDER_NUMBER = next_order_number

        return str(next_order_number)

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        DMcC 15/02/24 would like this only to apply when status = ORDERED or PACKED.
        As deleting a historical product master can mean the order total
        recalculates for historical orders
        """
        print(f'In order.update_total, order ', self.order_number)
        if self.order_status not in ['SHIPPED', 'RECEIVED']:
            print(f'Order at status {self.order_status}'
                  + 'will not be affected by product removal')
            self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
            if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
                self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
            else:
                self.delivery_cost = 0
            self.grand_total = self.order_total + self.delivery_cost
            self.save()
        else:
            print(f'Order at status {self.order_status},'
                  + 'will not be affected by product removal')

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

    def order_ship_date(self):
        """ calculate the order shipping date based on the """
        """ latest order line ship date    """
        latest_line_ship_date = self.lineitems.aggregate(Max('line_ship_date'))['line_ship_date__max']
        return (latest_line_ship_date or
                datetime.date(2024, 2, 28).time(0, 0, 0))


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    line_number = models.IntegerField(default=10)
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE, 
                                related_name='orderlines')
    sku = models.CharField(max_length=20, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2,
                                null=True, blank=True)
    category = models.CharField(max_length=30, null=True, blank=True)
    product_size = models.CharField(max_length=1,
                                    choices=RING_SIZE_CHOICES,
                                    default=' ')
    can_be_engraved = models.BooleanField(default=False)
    engrave_text = models.CharField(max_length=100, null=True, blank=True)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)
    line_ship_date = models.DateField(default=(datetime.date.today()
                                      + timedelta(days=5)))

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total,
        set the line number,
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        if not self.line_number:
            self.order_line = self._generate_line_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return (f'SKU {self.product.sku} on order {self.order.order_number}'
                + f' line number {self.line_number}')

    def _generate_line_number(order):
        """
        Generate a next number for the line# for a given order,
        based on increments of 10 from the last order line saved
        for this order.
        Else if no orders on table, then use settings.FIRST_LINE_NUMBER
        """
        print("In function generate_Line_number for order ", order)
        orderlines = OrderLineItem.objects.filter_by(order)
        if (OrderLineItem.objects.filter_by(order).order_by('line_number').last()):
            max_line_number = (OrderLineItem.objects.filter_by(order).
                               order_by('line_number').last().line_number)
            print(f"highest line # on this order is ", {max_line_number})
            next_line_number = int(max_line_number) + 10
            print(f"next line # on this order is ", next_line_number)
        else:
            next_line_number = settings.FIRST_LINE_NUMBER

        return str(next_line_number)

    def item_ship_date(self):
        now = timezone.now().time(0, 0, 0)
        product_delta = int(self.product.lead_time)
        print(f'Product ', {self.product}, 'lead_time is ', {product_delta})
        print(f'ship date calc: ', {now + timedelta(days=product_delta)})
        return now + timedelta(days=product_delta)


class OrderAddress(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              related_name="order_address")
    address_type = models.CharField(max_length=4, null=False,
                                     editable=True, default='BILL')
    address_id = models.CharField(max_length=4, null=False, editable=False)
    address_label = models.CharField(max_length=25, null=True, blank=True)
    address1 = models.CharField(max_length=80, null=True, blank=True)
    address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'{self.order}__{self.address_type}__{self.address_id}'
                + f'__{self.address_label}__{self.address1}__{self.address2}'
                + f'__{self.postcode}__{self.created_on}')

    class Meta:
        """ returns addresses sorted on order# address_id,created_on """
        ordering = ['order', 'address_type', 'address_id', 'created_on']
