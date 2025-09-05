from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth import authenticate, logout 
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm
from .forms import ListForm
# Create your views here.
def Signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            # Set additional fields
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.save()
            
            messages.success(request, 'Account created successfully!')
            return redirect('Login')
    else:
        form = SignUpForm()
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
                return redirect('welcome')
            else:
                form=LoginForm()
    return render(request, 'records/login.html', {'form': form}) 

def Logout(request):    
    return HttpResponse('ok')


def welcome(request):
    return render(request,'records/welcome.html')


def createlist(request):
    form = ListForm()
    if request.method == 'POST':
        form = ListForm(request.POST,request.FILES)
        if form.is_valid():
            create = form.save(commmit=False)
            create.user = request.user
            create.save()
            return redirect('showlist')
        else:
            form = ListForm()
    return render(request,'records/createlist')