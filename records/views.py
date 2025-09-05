from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect,get_object_or_404
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth import authenticate, logout 
from django.contrib.auth.forms import UserCreationForm
from . import forms,models

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
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}.')
                return redirect('welcome')
            else:
                form=forms.LoginForm()
    return render(request, 'records/login.html', {'form': form}) 

def Logout(request):    
    return HttpResponse('ok')


def welcome(request):
    return render(request,'records/welcome.html')


def createlist(request):
    form = forms.ListForm()
    if request.method == 'POST':
        form = forms.ListForm(request.POST,request.FILES)
        if form.is_valid():
            create = form.save(commit=False)
            create.user = request.user
            create.save()
            return redirect('showlist')
        else:
            form = forms.ListForm()
    else :
        form = forms.ListForm()
        return render(request,'records/createlist.html',{'form':form})
    
def showlist(request):
    lists = models.List.objects.all()   # fetch all List objects
    return render(request, 'records/showlist.html', {'lists': lists})

def edit(request,id ):
    xx =  get_object_or_404(models.List, pk=id, created_by=request.user)
    if request.method == 'POST':
        form = forms.ListForm(request.POST,request.FILES,instance=xx)
        if form.is_valid():
            return redirect ('showlist')
        else :
            form = forms.ListForm(instance=xx)
            return render(request,'records/createlist.html',{'form':form})
    else:
        form = forms.ListForm(instance=xx)
        x = 1 
        return render(request,'records/createlist.html',{'form':form, 'x' : x })
        

