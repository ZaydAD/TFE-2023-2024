from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profile
from .models import Messages


class UserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter firstname'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter lastname'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]


class ProfileForm(ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter firstname'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter lastname'}))

    class Meta:
        model = Profile
        fields = ["username", "email", "first_name", "last_name", "picture"]


class MessageForm(forms.ModelForm): #not used "failed websocket connection"
    class Meta:
        model = Messages
        fields = ["message"]
    