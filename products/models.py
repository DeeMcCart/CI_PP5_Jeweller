from django.db import models
from profiles.models import UserProfile
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

ITEM_SOURCE_CHOICES = [
    ('STOCK', 'Stocked Item'),
    ('MTO', 'Make-to-Order'),
    ('COMM', 'Comission/ One-off'),
    ('SERV', 'Service'),
    ('PERS', 'Personalisation')
]
class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    hide_display = models.BooleanField(default = False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cat6_value = models.ForeignKey('Cat6', null=True, blank=True, on_delete=models.SET_NULL)
    source = models.CharField(max_length=5, choices=ITEM_SOURCE_CHOICES, default='STOCK')
    item_lead_time = models.IntegerField(default=0)
    promotion = models.CharField(max_length=10, null=True, blank = True)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    description = models.TextField()
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def lead_time(self):
        """ return lead time for product, if not set """ 
        """ on product use from category leadtime """
        if self.item_lead_time != 0:
            return (self.item_lead_time)    
        else:
            return (self.cat6_value.default_lead_time)
            
class Catname(models.Model):
    cat_num = models.IntegerField()
    cat_name = models.CharField(max_length=15)
    nice_name = models.CharField(max_length=50, null=True, blank=True)
    default_display = models.BooleanField(default=True)

    def __str__(self): 
        return f'{self.cat_num}------{self.cat_name}------{self.nice_name}'

    def get_nice_name(self):
        return self.nice_name


class Cat5(models.Model):
    cat5_value = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f'{self.cat5_value}'

class StockType(models.Model):
    stock_type = models.CharField(max_length=30, null=True, blank=True)
    default_lead_time = models.IntegerField()

    def __str__(self):
        return f'{self.stock_type}'


class Cat6(models.Model):
    cat6_value = models.CharField(max_length=30, null=True, blank=True)
    stock_type = models.CharField(max_length=30, null=True, blank=True, default='STOCK')
    default_lead_time = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.stock_type}'

class Review(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviews') 
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=30, null=False, blank=False)
    body = models.CharField(max_length=254, null=False, blank=False)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True) 
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Review {self.rating} {self.body} by {self.user_profile}"