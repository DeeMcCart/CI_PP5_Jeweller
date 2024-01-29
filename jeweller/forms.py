# created custom forms.py to hold a custom user signup form 
#
from django import forms
from profiles.models import UserProfile
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    phone_number_1 = forms.CharField(max_length=15, label='Mobile')
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    newsletter_signup = forms.BooleanField 
    
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.last_name = self.cleaned_data['last_name']
        user.first_name = self.cleaned_data['first_name']
        user.save()
        return user

    class Meta:
        model = UserProfile
        fields = ('username', 'phone_number1', 'first_name', 'last_name', 'password1', 'password2',)
