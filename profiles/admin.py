from django.contrib import admin
from .models import UserProfile, UserAddress, create_or_update_user_profile
from django.db.models.signals import post_save

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserAddress)

# DMcC 05/02/24:  Register the post_save connect so that User Prfiles can be automatically created
# post_save.connect(create_or_update_user_profile)