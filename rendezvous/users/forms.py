from django import forms
from .models import MyUser, FriendRequest


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'username']


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'password']
