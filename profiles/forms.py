from django import forms
from .models import UserProfile, UserAddress
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
        
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        # DMcC troubleshooting 05/02/24 - appears the init function working OK as getting a placeholder image for new User Profiles
        # however not getting the values from here into the form 
        super().__init__(*args, **kwargs)
        placeholders = {
            'user': 'user',
            'phone_number1': 'Phone Number',
            'phone_number2': 'Alt Phone',
            'profile_image': "../../static/images/placeholder.png",
            'birth_month': '00',
            'newsletter_signup': False,
             }
        # self.fields['phone_number1'].widget.attrs['autofocus'] = True
        
        for field in self.fields:
            if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False

class UserAddressForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        fields = ('user', 'address_type', 'address_label', 'address1') 
        
        
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'address_type' : 'DEL',
            'address_id' : '10',
            'address_label' : 'Home',
            'address1': 'Street Address 1',
            'address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'county': 'County',
            'postcode': 'Postal Code',
            'country': 'IE',
        }

        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False






