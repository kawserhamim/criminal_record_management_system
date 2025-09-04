from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth import authenticate, logout as auth_logout

# Create your views here.
def Signup(request):
    if request.method =='POST' :
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('User created successfully')
        else:
            form = SignUpForm()
    return render(request, 'records/signup.html', {'form': form})
def Login(request): 
    return HttpResponse('ok')   
def Logout(request):    
    return HttpResponse('ok')
