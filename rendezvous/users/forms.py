from django import forms
from .models import User, FriendRequest


class UserRegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']
