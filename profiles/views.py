from django.contrib import messages
from django.shortcuts import render, get_object_or_404, reverse, redirect
from home.models import Contact
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def register(request):
    context = {}
    if request.method == "POST":
        # Fetch data from HTML form
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        contact = request.POST.get('number')
        check = User.objects.filter(username=email)
        if len(check) == 0:
            # Save data to both tables
            usr = User.objects.create_user(email, email, password)
            usr.first_name = name
            usr.save()

            profile = Profile(user=usr, contact_number=contact)
            profile.save()
            context['status'] = f"User {name} Registered Successfully!"
        else:
            context['error'] = "A User with this email already exists"

    return render(request, 'home/register.html', context)


def check_user_exists(request):
    email = request.GET.get('usern')
    check = User.objects.filter(username=email)
    if len(check) == 0:
        return JsonResponse({'status': 0, 'message': 'Not Exist'})
    else:
        return JsonResponse({'status': 1, 'message':
                            'A user with this email already exists!'})


def signin(request):
    context = {}
    if request.method == "POST":
        email = request.POST.get('email')
        passw = request.POST.get('password')

        check_user = authenticate(username=email, password=passw)
        if check_user:
            login(request, check_user)
            if check_user.is_superuser or check_user.is_staff:
                return HttpResponseRedirect('/admin')
            return HttpResponseRedirect('/dashboard')
        else:
            context.update({'message': 'Invalid Login Details!',
                           'class': 'alert-danger'})

    return render(request, 'home/login.html', context)


def dashboard(request):
    context = {}
    login_user = get_object_or_404(User, id=request.user.id)
    # Fetch login user's details
    profile = Profile.objects.get(user__id=request.user.id)
    context['profile'] = profile

    # Update profile
    if "update_profile" in request.POST:
        print("file=", request.FILES)
        name = request.POST.get('name')
        contact = request.POST.get('contact_number')
        add = request.POST.get('address')

        profile.user.first_name = name
        profile.user.save()
        profile.contact_number = contact
        profile.address = add

        if "profile_pic" in request.FILES:
            pic = request.FILES['profile_pic']
            profile.profile_pic = pic
        profile.save()
        context['status'] = 'Profile updated successfully!'
    # Change Password
    if "change_pass" in request.POST:
        c_password = request.POST.get('current_password')
        n_password = request.POST.get('new_password')

        check = login_user.check_password(c_password)
        if check is True:
            login_user.set_password(n_password)
            login_user.save()
            login(request, login_user)
            context['status'] = 'Password Updated Successfully!'
        else:
            context['status'] = 'Current Password Incorrect!'

    # My Orders
    # context['orders'] = orders

    return render(request, 'home/profile.html')
