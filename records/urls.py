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
    path('createlist/', views.createlist, name='createlist'),
    path('showlist/', views.showlist, name='showlist'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('search/', views.search, name='search'),
    path('mycreate/', views.mycreate, name='mycreate'),
    
]
