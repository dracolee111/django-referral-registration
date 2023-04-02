# -*- encoding: utf-8 -*-

# Create your views here.
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from .models import referral_program
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

User = get_user_model()


def login_view(request):
    """
    Logs in the user if credentials are valid using the ``authenticate()`` function from the ``AUTHENTICATION_BACKENDS``
    defined in ``settings.py.``

    * if a ``next_url`` is given in the url query parameter, override the default ``LOGIN_REDIRECT_URL`` 
    defined in ``settings.py``
    """
    msg = None
    user = request.user
    next_url = request.GET.get('next')
        
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect('profile.html')
            else:
                msg = 'Invalid credentials'
    else:
        form = LoginForm()
        if user.is_authenticated:
            return redirect('profile.html')
    return render(request, "accounts/login.html", {"form": form, "msg": msg})




def register_user(request):
    """
    User registration view using the ``AUTH_USER_MODEL`` defined in ``settings.py``.
    It also has the following features:
         * user registration.
         * referral code validation.
         * referral field creation.
         * sends welcome email to the user.
         * sends activation link if needed using the ``send_activation_code()`` function.
    """
    if request.user.is_authenticated:
        return redirect('profile.html')
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password1']
            referral_code = form.cleaned_data.get('referral_code')

            # Check if referral code is valid
            referred_by = None
            if referral_code:
                try:
                    referred_by = User.objects.get(username=referral_code)
                except ObjectDoesNotExist:
                    form.add_error('referral_code', 'Invalid referral code')
                    return render(request, 'accounts/register.html', {'form': form})

            # Create user
            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password,
                referred_by=referred_by,
            )

            ### Send welcome message
            subject = f'Hello there!'
            message = render_to_string('accounts/welcome_email.html')
            email = EmailMessage(
                subject=subject,
                body=message,
                to=[email],
                from_email='help@example.com'
                )
            email.send()


            # If user was referred, create referral field
            if referred_by:
                referral = referral_program.objects.create(referrals=user, user=referred_by)
                referral.save()

            return render(request, 'accounts/register_done.html')
    else:
        # Get referral code from URL query parameter
        referral_code = request.GET.get('ref')
        form = SignUpForm(initial={'referral_code': referral_code})
    return render(request, 'accounts/register.html', {'form': form, 'msg': msg})
