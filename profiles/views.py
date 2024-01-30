from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import UserProfile
# from checkout.models import Order
from django.contrib import messages
from .forms import UserProfileForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import default_storage

# Create your views here.

def profile(request):
    """ Display the user's profile. """
    print(f"In views def profile(request).  Request is ", request)
    profile = get_object_or_404(UserProfile, user=request.user)
    if profile:
        if request.method=="GET":
            print(f"Profile ", profile, "retrieved successfully")
            form = UserProfileForm(instance=profile)
            return profile
        else: 
            if request.method == 'POST':
                form = UserProfileForm(request.POST, instance=profile)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Profile updated successfully')
                else:
                    messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        print(f"Profile ", profile, "NOT retrieved")
        print(f"No profile retrieved")
        messages.error(request, 'Update failed. Please ensure the form is valid.')
        return(profile)      



