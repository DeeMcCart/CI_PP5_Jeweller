from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        # call the default init method to set up the form as it would be by default
        super().__init__(*args, **kwargs)
        # set placeholders as prompts for entry
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }
        # first focus is on the full name field when the page is loaded
        self.fields['full_name'].widget.attrs['autofocus'] = True
        # iterate through form fields add a * if field is required by the model
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
            # set the value of the field to placeholder value
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # add a css class for later use
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # remove form label fields
            self.fields[field].label = False