from django.contrib import admin
from .models import Product, Category, Cat0, Cat1, Cat2, Cat3, Cat4, Cat5, Cat6, Catname

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
        'cat_nice_name',
        )
    ordering='cat_num'

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'created_on',
    )

    ordering = ('sku',)




admin.site.register(Product, Category, Catname, Cat0, Cat1, Cat2, Cat3, Cat4, Cat5, Cat6)