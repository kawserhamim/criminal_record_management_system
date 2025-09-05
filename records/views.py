from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth import authenticate, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm

# Create your views here.
def Signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully!')
            return HttpResponse('ok')
    else:
        form = UserCreationForm()
    return render(request, 'records/signup.html', {'form': form})
def Login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}.')
                return HttpResponse('ok')
            else:
                form=LoginForm()
    return render(request, 'records/login.html', {'form': form}) 

def Logout(request):    
    return HttpResponse('ok')
