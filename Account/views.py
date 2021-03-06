from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
# Create your views here.
from .forms import AccountAuthenticationForm, RegistrationForm, ProfileForm
from .models import Account, Profile


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("home")

    else:
        form = AccountAuthenticationForm()
        context['login_form'] = form

    return render(request, "login.html", context)


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print("success")
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect("home")
        else:
            context['registration_form'] = form
            return render(request, 'register.html', context)

    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'register.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


def dashboard(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return render(request, "dashboard.html", context)
        