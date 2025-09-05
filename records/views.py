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
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            department = form.cleaned_data.get('department')
            badge_number = form.cleaned_data.get('badge_number')
            remember_me = form.cleaned_data.get('remember_me')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                # Check if department and badge number match
                if user.department == department and user.badge_number == badge_number:
                    login(request, user)
                    if not remember_me:
                        request.session.set_expiry(0)
                    messages.success(request, f'Welcome back, {username}!')
                    return HttpResponse('ok')
                else:
                    messages.error(request, 'Invalid department or badge number.')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'records/login.html', {'form': form}) 
def Logout(request):    
    return HttpResponse('ok')
