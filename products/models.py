from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    cat0_value = models.ForeignKey('Cat0', null=True, blank=True, on_delete=models.SET_NULL)
    cat1_value = models.ForeignKey('Cat1', null=True, blank=True, on_delete=models.SET_NULL)
    cat2_value = models.ForeignKey('Cat2', null=True, blank=True, on_delete=models.SET_NULL)
    cat3_value = models.ForeignKey('Cat3', null=True, blank=True, on_delete=models.SET_NULL)
    cat4_value = models.ForeignKey('Cat4', null=True, blank=True, on_delete=models.SET_NULL)
    cat5_value = models.ForeignKey('Cat5', null=True, blank=True, on_delete=models.SET_NULL)
    cat6_value = models.ForeignKey('Cat6', null=True, blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f'{self.category}.....{self.name}.....Categories: {self.cat0_value}; {self.cat1_value}; {self.cat2_value}; {self.cat3_value}; {self.cat4_value}; {self.cat5_value}; {self.cat6_value}'
        

class Catname(models.Model):
    cat_num = models.IntegerField()
    cat_name = models.CharField(max_length=15)
    nice_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self): 
        return f'{self.cat_num}------{self.cat_name}------{self.nice_name}'

    def get_nice_name(self):
        return self.nice_name


class Cat0(models.Model):
    cat0_value = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f'{self.cat0_value}'

class Cat1(models.Model):
    cat1_value = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f'{self.cat1_value}'
        
class Cat2(models.Model):
    cat2_value = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f'{self.cat2_value}'

class Cat3(models.Model):
    cat3_value = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f'{self.cat3_value}'


class Cat4(models.Model):
    cat4_value = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f'{self.cat4_value}'

class Cat5(models.Model):
    cat5_value = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f'{self.cat5_value}'

class Cat6(models.Model):
    cat6_value = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f'{self.cat6_value}'
