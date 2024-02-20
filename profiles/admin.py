from django.contrib import admin
from .models import UserProfile, UserAddress, create_or_update_user_profile
from django.db.models.signals import post_save


# DMcC 05/02/24:  Register the post_save connect so that 
# User Profiles can be automatically created
# post_save.connect(create_or_update_user_profile)

class UserAddressAdminInline(admin.TabularInline):
    model = UserAddress


class UserProfileAdmin(admin.ModelAdmin):
    inlines = (UserAddressAdminInline,)

    readonly_fields = ('created_on',)

    fields = ('user', 'phone_number1', 
              'profile_image', 'newsletter_signup',)

    list_display = ('user', 'phone_number1', 
                    'profile_image', 'newsletter_signup', 'created_on',)

    ordering = ('user',)

# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
