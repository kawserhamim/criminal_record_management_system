from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
# Make sure you import your custom Profile model


class SignUpForm(UserCreationForm):
    # These fields will be displayed on the form
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    department = forms.CharField(max_length=100, required=True)
    badge_number = forms.CharField(max_length=50, required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        # Only include the fields that exist on the User model
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'department', 'badge_number'  )

    # This method runs after the form is submitted and validated 
    def save(self, commit=True):
        # First, save the basic user information (username, password)
        user = super().save(commit=False)

        # Then, add the first name, last name, and email
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.department=self.cleaned_data['department'],
        user.badge_number=self.cleaned_data['badge_number']
       
        
        if commit:
            # Save the user to the database
            user.save()
            
            # Now, create a new profile for the user with the extra data
          

        return user
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'required': True
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'required': True
        })
    )
    department = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Department Name',
            'required': True
        })
    )
    badge_number = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Badge Number',
            'required': True
        })
    )
    remember_me = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        })
    )