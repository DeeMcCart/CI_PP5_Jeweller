# created custom forms.py to hold a custom user signup form
#
from django import forms
from django.shortcuts import get_object_or_404
from django.contrib import messages
from profiles.models import UserProfile
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
import time


class CustomSignupForm(SignupForm):
    """ Gather additional fields first & last name for allauth User
        and phone number for UserProfile
    """
    first_name = forms.CharField(max_length=15, label='First Name')
    last_name = forms.CharField(max_length=15, label='Last Name')
    phone_number = forms.CharField(max_length=15, label='Mobile')

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'phone_number',
            'last_name',
            'email',
            'password1',
            )

    # Added init method to assign/show default values and save screen space
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['first_name'] = 'First'
        self.initial['last_name'] = 'Last'
        self.initial['phone_number'] = 'Tel'

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

#       Retrieve user profile (auto created by signal using default values)
#       when User is created
        user_profile = get_object_or_404(UserProfile, user=user)
        if user_profile:
            # Add in the phone number data from the form field
            user_profile.phone_number1 = self.cleaned_data['phone_number']
            # DMcC 20/02/24 introduced small time delay pre save attempt
            time.sleep(1)
            user_profile.save()
            user_profile_upd = get_object_or_404(UserProfile, user=user)
            messages.success(request, f'UserProfile {user.username} \
                                        {user_profile_upd.phone_number1} \
                                        created')
        return user
