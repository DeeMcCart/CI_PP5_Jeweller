from django.contrib import admin
from .models import (UserProfile, UserAddress)


class UserAddressAdminInline(admin.TabularInline):
    model = UserAddress


class UserProfileAdmin(admin.ModelAdmin):
    inlines = (UserAddressAdminInline,)

    readonly_fields = ('created_on',)

    fields = ('user', 'phone_number1',
              'profile_image', )

    list_display = ('user', 'phone_number1',
                    'profile_image', 'created_on',)

    ordering = ('user',)


# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
