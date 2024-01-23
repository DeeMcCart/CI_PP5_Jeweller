from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField

    
# Create your models here.
class UserProfile(models.Model):
    """ UserProfile class extends allauth User models
    includes profile_image, can be linked to delivery addresses 
    and order history """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number1 = models.CharField(max_length=20, null=True, blank=True)
    phone_number2 = models.CharField(max_length=20, null=True, blank=True)
    profile_image = CloudinaryField('image', default='placeholder')
    birth_month = models.CharField(max_length=9, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        """ set ordering of user profiles to most recent first """
        ordering = ['-created_on']
        
    
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile    """

    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()

class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_address")
    address_type =  models.CharField(max_length=4, null=False, editable=True)
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
        return self.user_profile, self.address_id, self.address_label

    class Meta:
         """ returns addresses sorted on user then address_id, then  as tie-breaker """
         ordering = ['user', 'address_id', 'created_on']        