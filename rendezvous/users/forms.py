from django import forms
from .models import MyUser, FriendRequest


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = MyUser
        username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=120)
        first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=120)
        last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=120)
        password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
        fields = ['first_name', 'last_name', 'username', 'password']


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = MyUser
        username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=120)
        password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
        fields = ['username', 'password']
