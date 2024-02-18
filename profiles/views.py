from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile, UserAddress
from .forms import UserProfileForm
from checkout.models import Order
from jeweller.forms import CustomSignupForm
from django.contrib.auth.decorators import login_required


# Create your views here.
# DMcC 09/02/24 Add @login_required decorator to ensure user logged in
@login_required
def profile_detail(request, profile_id):
    """ A view to return a specific profile id """
    if (request.user.is_authenticated
        and (profile_id == request.user.userprofile.id)
        or (request.user.is_superuser)):

        current_profile = get_object_or_404(UserProfile, id=profile_id)
        current_user = get_object_or_404(User, username=current_profile.user)
        # removed the message below as it appears only when the button is
        # pressed, and is confusing to the user
        # messages.info(request, (f'Editing user profile
        # for {current_profile.user}'))

        if request.method == 'POST':
            # user_form = CustomSignupForm(request.POST, request.FILES or None,
            # instance=current_user)
            profile_form = UserProfileForm(request.POST, request.FILES or None,
                                           instance=current_profile)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Profile updated successfully')
                return redirect(reverse('profile_detail',
                                        args=[current_profile.id]))
            else:
                messages.error(request, 'Update failed. Please ensure '
                               + 'the form is valid.')
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
    else:
        messages.error(request, 'Restricted: Must have SysAdmin rights to edit'
                       + ' other users profile!')
        return redirect(reverse('home'))


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is order {order_number}, '
        f'status {order.order_status}.'
        ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def add_profile(request):
    """ On registration:  Create a new user profile """

    if request.method == 'POST':
        print("In profiles/views/add_profile")
        profile_form = ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile = profile_form.save()
            # return an informative success message
            stringy = (f'Successfully added user profile '
                       + f'{request.user.user_profile},'
                       + f'{request.user.user_profile.phone_number1}')
            messages.success(request, stringy)
            # show new product so sysadmin can visually confirm
            template = 'profiles/profile.html'
            context = {'form': profile_form,
                       'on_profile_page': True,
                       }

            return render(request, template, context)
        else:
            messages.error(request, 'Failed to add profile.'
                           + 'Please ensure the form is valid.')
    else:
        template = 'profiles/profile.html'
        context = {
            'form': profile_form,
            'on_profile_page': True,
        }

        return render(request, template, context)
