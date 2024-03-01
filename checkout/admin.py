from django.contrib import admin

# Register your models here.
from .models import Order, OrderLineItem, OrderAddress


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAddressAdminInLine(admin.TabularInline):
    model = OrderAddress


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline, OrderAddressAdminInLine)

    readonly_fields = ('order_number', 'user_profile', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_basket', 'stripe_pid')

    fields = ('order_number', 'order_status', 'user_profile', 'date',
              'full_name', 'email', 'phone_number', 'planned_ship_date',
              'delivery_method', 'delivery_track', 'postcode', 'town_or_city',
              'street_address1', 'street_address2', 'county',
              'order_total', 'delivery_cost', 'grand_total',
              'original_basket', 'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin, )
