from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import fields
import random

class UserForm(UserCreationForm):
    username = forms.CharField()
    password = forms.CharField()
    confirm_password = forms.PasswordInput()
    ans=forms.IntegerField()
    class Meta:
        model=User
        fields=('username','password1','password2')

class EditForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','date_joined','last_login']
        labels={'email':'Email'}

