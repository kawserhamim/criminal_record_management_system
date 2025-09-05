from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import render, redirect   
from django.contrib import messages


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=15,required=True
                                 ,widget=forms.TextInput(
                                     attrs={
                                            'class': 'form-control',
                                            'placeholder': 'First Name' 
                                     }
                                 ))
    last_name = forms.CharField(max_length=15,required=True
                                ,widget=forms.TextInput(            
                                    attrs={
                                           'class': 'form-control',
                                           'placeholder': 'Last Name' 
                                    }
                                ))
    email = forms.EmailField(max_length=50,required=True
                             ,widget=forms.EmailInput(
                                 attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Email' 
                                 }
                                ))
  
    
    class Meta :
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')
    def save(self, commit=True):
      user = super().save(commit=False)
      user.first_name = self.cleaned_data['first_name']
      user.last_name = self.cleaned_data['last_name']
      user.email = self.cleaned_data['email']
      if commit:
         user.save()
      return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))