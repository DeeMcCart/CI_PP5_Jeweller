from django.shortcuts import render, get_object_or_404
from .models import UserProfile
# from checkout.models import Order
from django.contrib import messages
from .forms import UserProfileForm

# Create your views here.

def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    addresses = profile.UserAddress.all()
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'adresses': addresses,
        'on_profile_page': True,}
    return render(request, template, context)