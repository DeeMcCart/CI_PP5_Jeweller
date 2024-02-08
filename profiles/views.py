from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile
from checkout.models import Order
from .forms import UserProfileForm
from jeweller.forms import CustomSignupForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required

# Create your views here.
  
# DMcC 09/02/24 Add @login_required decorator to ensure user logged in
@login_required
def profile(request):
    """ Display or update the user's profile. """
    if request.user.is_authenticated:
        current_profile = get_object_or_404(UserProfile, user=request.user)
        current_user = get_object_or_404(User, username=request.user)
       
    if request.method == 'POST':
        # user_form = CustomSignupForm(request.POST, request.FILES or None, instance=current_user)
        profile_form = UserProfileForm(request.POST, request.FILES or None, instance=current_profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        profile_form = UserProfileForm(instance=current_profile)
    
    # retrieve historical orders linked to this user profile
    orders = current_profile.orders.all().order_by('-order_number')
    # retrieve all addresses linked to this user profile
    addresses = current_profile.user_address.all()

    template = 'profiles/profile.html'
    context = {
        'form': profile_form,
        'orders': orders,
        'addresses': addresses,
        'on_profile_page': True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}.'
        'A confirmation email was sent on the order date.'
        ))
        
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
            

