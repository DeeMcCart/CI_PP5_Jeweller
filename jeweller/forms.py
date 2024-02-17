# created custom forms.py to hold a custom user signup form
#
from django import forms
from profiles.models import UserProfile, create_or_update_user_profile
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from profiles.forms import UserProfileForm
from products.widgets import CustomClearableFileInput


class CustomSignupForm(SignupForm):
    """ Gather additional fields first & last name for allauth user
    """
    # DMcC 09/02/24:  Apply our lovely widget to improve clunky apperance of image
    first_name = forms.CharField(max_length=15, label='First Name')
    last_name = forms.CharField(max_length=15, label='Last Name')
    phone_number_1 = forms.CharField(max_length=15, label='Mobile')
    # profile_image = forms.ImageField(label='Image', required=False,
    #                                 widget=CustomClearableFileInput)
    newsletter_signup = forms.TypedChoiceField(
        label='Sign up for Newsletter?',
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '0',
        required = True,
    )


    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        print(f'User ', user.first_name, ' ', user.last_name, ' created')

#        user_profile = UserProfileForm.save(request)
#       create_or_update_user_profile(User, user, True)
#       Pass the sender, instance and created flag
 
#        user_profile.user = self.cleaned_data['username']

#       DMcC 17/02/24:
#       Retrieve user profile (auto created by signal using default values)
#       when User is created
        user_profile = get_object_or_404(userProfile, user=user)
#       Add in the phone number data from the form field
        user_profile.phone_number1 = self.cleaned_data['phone_number1']
        user_profile.save()       
#        user_profile.phone_number2 = self.cleaned_data['phone_number1']
#        user_profile.profile_image = self.cleaned_data['profile_image']
#        user_profile.newsletter_signup = False
#        add_profile(request)        return user

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            )
