from django.urls import path
from . import views
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
urlpatterns = [
    
    path('Signup/', views.Signup, name='Signup'),
    path('Login/', views.Login, name='Login'),
    path('Logout/', views.Logout, name='Logout'),
    path('welcome/', views.welcome, name='welcome'),
    
]
