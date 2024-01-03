from django import forms
from django.contrib.auth import authenticate
from authentication.models import userInformation
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text="Required. Add a valid email address")


    class Meta:
        model = userInformation
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password",      
        )

class AccountAuthenticationForm(forms.ModelForm):

    class Meta:
        model = userInformation
        fields = ('username','password')
    
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Your Are Not a Valid User")