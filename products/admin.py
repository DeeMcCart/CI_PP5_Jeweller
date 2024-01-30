from django.contrib import admin
from .models import Product, Category, Cat1, Cat2, Cat3, Cat4

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )




admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cat1)
admin.site.register(Cat2)
admin.site.register(Cat3)
admin.site.register(Cat4)