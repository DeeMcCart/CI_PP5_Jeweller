# created custom forms.py to hold a custom user signup form
#
from django import forms
from profiles.models import UserProfile, create_or_update_user_profile
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from profiles.forms import UserProfileForm
from products.widgets import CustomClearableFileInput


class CustomSignupForm(SignupForm):
    """ Used to hold the combined User and UserProfile fields
    This begins with the additional fields needed for the UserProfile
    """
    # phone_number_1 = forms.CharField(max_length=15, label='Mobile')
    # DMcC 09/02/24:  Apply our lovely widget to improve clunky apperance of image
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    profile_image = forms.ImageField(label='Image', required=False,
                                     widget=CustomClearableFileInput)
    # newsletter_signup = forms.BooleanField(label='Newsletter')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        print(f'User ', user.first_name, ' ', user.last_name, ' created')

#       DMcC 06/02/24 getting a WSGI error on new user profile creation
#       (but it is getting created with default values )
#       Try delaying the commit to see if this makes a difference

        user_profile = UserProfileForm.save(request)
#       create_or_update_user_profile(User, user, True)
#       Pass the sender, instance and created flag
#       user_profile = get_object_or_404(UserProfile, user=user)

        user_profile.user = self.cleaned_data['username']
        user_profile.phone_number1 = self.cleaned_data['phone_number1']
        user_profile.phone_number2 = self.cleaned_data['phone_number1']
        user_profile.profile_image = self.cleaned_data['profile_image']
        user_profile.newsletter_signup = False
        user_profile.save()       
        add_profile(request)
        return user

    class Meta:
        model = User
        fields = (
            'username',
            'phone_number1',
            'first_name',
            'last_name',
            'email',
            'profile_image',
            'password1',
            'password2',)
