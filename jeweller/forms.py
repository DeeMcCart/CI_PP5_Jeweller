# created custom forms.py to hold a custom user signup form 
#
from django import forms
from profiles.models import UserProfile
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from profiles.forms import UserProfileForm

class CustomSignupForm(SignupForm):
    phone_number_1 = forms.CharField(max_length=15, label='Mobile')
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    newsletter_signup = forms.BooleanField(label='Sign up for newsletter') 
        
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.last_name = self.cleaned_data['last_name']
        user.first_name = self.cleaned_data['first_name']
        user.save()

        user_profile = UserProfileForm.save(request)
        user_profile.user=self.cleaned_data['username']
        user_profile.phone_number1=self.cleaned_data['phone_number1']
        user_profile.phone_number2='0591231234'
        user_profile.newsletter_signup=self.cleaned_data['newsletter_signup']
        user_profile.save()
        
        return user

    class Meta:
        model = User
        fields = (
            'username', 
            'phone_number1', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2',)
