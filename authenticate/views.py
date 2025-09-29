from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

from . import forms

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Rediriger vers la page principale de l'API
            else:
                form.add_error(None, "Nom d'utilisateur ou mot de passe incorrect.")
    else:
        form = forms.LoginForm()
    return render(request, 'authenticate/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Rediriger vers la page de connexion après la déconnexion

def signup_view(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Rediriger vers la page de connexion après l'inscription
    else:
        form = forms.SignUpForm()
    return render(request, 'authenticate/signup.html', {'form': form})

