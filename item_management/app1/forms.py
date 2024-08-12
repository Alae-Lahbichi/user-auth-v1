from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User



class userregister(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "Username"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder' : "Email"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : "Password"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : "Confirm password"
    }))
    class Meta :
        model = User
        fields =('username' , 'email' , 'password1' , 'password2')

class userlogin(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "username"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : "password"
    }))