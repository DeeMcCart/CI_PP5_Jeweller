from django import forms
from .models import UserProfile, UserAddress
from django.contrib.auth.models import User
from .widgets import CustomClearableFileInput


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    # DMcC 09/02/24:  Apply widget to improve clunky apperance of image
    profile_image = forms.ImageField(label='ProfileImage', required=False,
                                     widget=CustomClearableFileInput)

    
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and replace with placeholders, and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'user': 'user',
            'phone_number1': 'Tel',
            # change label for profile_image from 'profile_image': "../../static/images/placeholder.png",
            'profile_image': 'My Piccie',
            }
        self.fields['phone_number1'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if self.fields[field].required:
                print(f'field ',field, ' is required')
                placeholder = f'{placeholders[field]} *'
            else:
                print(f'field ',field, 'not required')
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = ('border-black rounded-0'
                                                        + ' profile-form-input')
        #    self.fields[field].label = False


class UserAddressForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        fields = ('user_profile', 'address_type', 'address_label', 'address1')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'address_type': 'DEL',
            'address_id': '10',
            'address_label': 'Home',
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
            self.fields[field].widget.attrs['class'] = ('border-black rounded-0'
                                                        + 'profile-form-input')
            self.fields[field].label = False
