from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Make sure you import your custom Profile model
from .models import Profile

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
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')

    # This method runs after the form is submitted and validated 
    def save(self, commit=True):
        # First, save the basic user information (username, password)
        user = super().save(commit=False)

        # Then, add the first name, last name, and email
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
       
        
        if commit:
            # Save the user to the database
            user.save()
            
            # Now, create a new profile for the user with the extra data
            Profile.objects.create(
                user=user,
                department=self.cleaned_data['department'],
                badge_number=self.cleaned_data['badge_number']
            )

        return user