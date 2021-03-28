from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser, FriendRequest


# class UserRegisterForm(forms.ModelForm):
#     class Meta:
#         model = MyUser
#         username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=120)
#         first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=120)
#         last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=120)
#         password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#         fields = ['first_name', 'last_name', 'username', 'password']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
