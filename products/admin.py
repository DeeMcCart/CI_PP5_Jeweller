from django.contrib import admin
from .models import Product, Category, Cat6, StockType, Catname, Review

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )


class CatnameAdmin(admin.ModelAdmin):
    list_display = (
        'cat_num',
        'cat_name',
        'nice_name',
        )

    ordering = ('cat_num',)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'can_be_engraved',
        'item_lead_time',
        'price',
        'rating',
        'created_on',
        'hide_display',
        'promotion',
        'image',
    )

    ordering = ('sku',)


class StockTypeAdmin(admin.ModelAdmin):
    list_display = (
        'source',
        'default_lead_time',
        )


class Cat6Admin(admin.ModelAdmin):
    list_display = (
        'cat6_value',
        'stock_type',
        'default_lead_time',
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'review_rating',
        'product',
        'title',
        'approved',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Catname, CatnameAdmin)
admin.site.register(Cat6, Cat6Admin)
admin.site.register(StockType, StockTypeAdmin)
admin.site.register(Review, ReviewAdmin)
