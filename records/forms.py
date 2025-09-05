from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from . import models

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder': "First Name"
        })
    )
    last_name = forms.CharField(
        max_length=30, required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder': "Last Name"
        })
    )
    email = forms.EmailField(
        max_length=254, required=True,
        widget=forms.EmailInput(attrs={
            'class': "form-control",
            'placeholder': "Email"
        })
    )
    national_id = forms.CharField(
        max_length=20, required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'placeholder': "National ID"
        })
    )
    badge_number = forms.CharField(
        max_length=50, required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder': "Badge Number"
        })
    )
    age = forms.CharField(
        max_length=3, required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder': "Age"
        })
    )
    phone = forms.CharField(
        max_length=15, required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder': "Phone Number"
        })
    )

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + (
            'first_name', 'last_name', 'email'
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Save additional profile info
            profile = models.Profile.objects.create(
                user=user,
                national_id=self.cleaned_data['national_id'],
                badge_number=self.cleaned_data['badge_number'],
                age=self.cleaned_data['age'],
                phone=self.cleaned_data['phone']
            )
        return user
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    national_id = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Department'}))
    badge_number = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Badge Number'}))
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'form-check-input'}))           