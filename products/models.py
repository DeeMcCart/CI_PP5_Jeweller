from django.db import models
from profiles.models import UserProfile
from django.shortcuts import get_object_or_404
from django.db.models import Avg
from datetime import date, timedelta


# Create your models here.


class Category(models.Model):
    """ category for products.  This sometimes has special meaning,
    e.g. category 'ring' will always have sizing """
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
    ('-', 'Not set'),
]


class Product(models.Model):
    """ Product class, extended from Boutique Ado walkthrough
    Extra fields:
        sku: Stock Keeping Unit;
        hide_display: prevent the product being
        shown or selected;
        can_be_engraved: indicates that a string of text up to length
        max_char_engrave can be associated with this products orderline;
        source: stock make-to-order, custom, service;
        item_lead_time: normally product lead times (used to derive orderline
        earliest ship dates) are calcualted based on the source, but an
        override value can be given here;
        promotion: if there is a promotion code linked to this product """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=254)
    hide_display = models.BooleanField(default=False)
    can_be_engraved = models.BooleanField(default=False)
    max_char_engrave = item_lead_time = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    source = models.CharField(max_length=5, choices=ITEM_SOURCE_CHOICES,
                              default='STOCK')
    item_lead_time = models.IntegerField(default=1)
    promotion = models.CharField(max_length=10, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    description = models.TextField()
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def lead_time(self):
        """ if lead time is set on product, return this value """
        """ otherwise derive lead time from SourceType leadtime """
        if self.item_lead_time != 0:
            return (self.item_lead_time)
        else:
            prod_source = self.source
            source = get_object_or_404(StockType, source=prod_source)
            lead_time = source.default_lead_time
            return (lead_time)

    def has_sizes(self):
        """ If the product is a ring then it has sizes """
        cat_name = str(self.category)
        if cat_name.strip() == "ring":
            return True
        else:
            return False

    def reviews(self):
        """ returns approved reviews for this product """
        return (self.reviews.filter(approved=True))

    def num_reviews(self):
        """ returns number of approved reviews for this product """
        return (self.reviews.filter(approved=True).count())

    def average_rating(self):
        """ returns average rating of approved reviews """
        apprvd_revs = self.reviews.filter(approved=True)
        if apprvd_revs.exists():
            avg_rating = (apprvd_revs.
                          aggregate(Avg('review_rating'))
                          ['review_rating__avg'])
            avg_rating = round(avg_rating, 1)  # Round to one decimal place
            return avg_rating
        else:
            print('No approved reviews found for average rating')
            return None  # Handle the case of no approved reviews gracefully

    def num_order_lines(self):
        """" return count of order lines for product else 0 """
        num_order_lines = 0
        if self.orderlines.count():
            return (self.orderlines.count())
        else:
            return (num_order_lines)

    def is_new(self):
        """ A simple view to determine if a product is < 10 days old """
        today = date.today()
        ten_days_ago = today - timedelta(days=10)
        date_created = self.created_on.date()
        if date_created >= ten_days_ago:
            # Product was created less than 10 days ago
            return True
        else:
            return False


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
    source = models.CharField(max_length=30, null=True, blank=True)
    models.CharField(max_length=5, choices=ITEM_SOURCE_CHOICES,
                     default='STOCK')
    default_lead_time = models.IntegerField()

    def __str__(self):
        return f'{self.source} {self.default_lead_time}'


class Cat6(models.Model):
    cat6_value = models.CharField(max_length=30, null=True, blank=True)
    stock_type = models.CharField(max_length=30, null=True, blank=True,
                                  default='STOCK')
    default_lead_time = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.stock_type}'


class Review(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='reviews')
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE,
                                related_name='reviews')
    title = models.CharField(max_length=30, null=False, blank=False)
    body = models.CharField(max_length=254, null=False, blank=False)
    review_rating = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=True, blank=True)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Review {self.review_rating} {self.body} - {self.user_profile}"
