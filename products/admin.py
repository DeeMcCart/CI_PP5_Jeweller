from django.contrib import admin
from .models import Product, Category, Cat5, Cat6, Catname, Review
from profiles.models import UserProfile

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

    ordering=('cat_num',)

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'cat5_value',
        'cat6_value',
        'price',
        'rating',
        'image',
        'created_on',
        'hide_display',
        'promotion',
    )

    ordering = ('sku',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Catname, CatnameAdmin)
admin.site.register(Cat5)
admin.site.register(Cat6)
admin.site.register(Review)