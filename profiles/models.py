from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from django.core.files.storage import FileSystemStorage


# Create your models here.
class UserProfile(models.Model):
    """ UserProfile class extends allauth User models
    includes profile_image, can be linked to delivery addresses
    and order history """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number1 = models.CharField(max_length=15, null=True, blank=True)
    # DMcC 20/02/24 remove phone_number2 as its a spurious field
    #     phone_number2 = models.CharField(max_length=15, null=True, blank=True)
    profile_image = models.ImageField(upload_to='images',
                                      default='placeholder.png')
    # DMcC 21/02/24 removed newsletter_signup as its been replaced by mailchimp
    # newsletter_signup = models.BooleanField(default=False)
    # DMcC removed birth_month as FUTURE feature
    # birth_month = models.CharField(max_length=9, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        """ order by recently created """
        ordering = ['-created_on']

# DMcC 07/02/24: Below is a signal this will ensure that whenever
# a User is created, a UserProfile is also created.
# Effectively this acts as a database trigger on save of User
# Note that this would normally sit in a separate signals.py file but
# incorporated here as relatively small code snippet


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """

    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()

# DMcC UserAddress is a child of UserProfile, and it has the ability to store
# multiple addresses per UserProfile.


class UserAddress(models.Model):
    user_profile = models.ForeignKey(UserProfile, null=False,
                                     on_delete=models.CASCADE,
                                     related_name="user_address")
    address_type = models.CharField(max_length=4, null=False, editable=True,
                                    default='BILL')
    address_id = models.CharField(max_length=4, null=False, editable=False,
                                  default='HOME')
    address_label = models.CharField(max_length=25, null=True, blank=True)
    address1 = models.CharField(max_length=80, null=True, blank=True)
    address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'{self.user_profile}__{self.address_type}__{self.address_id}'
                + f'{self.address_label}__{self.address1}__{self.address2}__'
                + f'{self.postcode}__{self.created_on};')

    class Meta:
        """ returns addresses sorted on user then address_id """
        ordering = ['user_profile', 'address_id', 'created_on']
