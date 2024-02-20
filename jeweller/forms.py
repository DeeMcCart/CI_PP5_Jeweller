# created custom forms.py to hold a custom user signup form
#
from django import forms
from django.shortcuts import get_object_or_404
from django.contrib import messages
from profiles.models import UserProfile, create_or_update_user_profile
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm

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
    
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
   
#       Retrieve user profile (auto created by signal using default values)
#       when User is created
        user_profile = get_object_or_404(UserProfile, user=user)
        if user_profile:
   
    #       Add in the phone number data from the form field
            user_profile.phone_number1 = self.cleaned_data['phone_number']
            user_profile.save()              
            messages.success(request, f'User {user.username} \
                                        {user_profile.phone_number1} \
                                        created') 
        return user

