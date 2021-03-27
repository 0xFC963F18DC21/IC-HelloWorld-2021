from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from ..accounts.models import UserProfile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'firstName',
            'lastName',
            'email',
            'password1'
        )

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.firstName = self.cleaned_data['firstName']
        user.lastName = self.cleaned_data['lastName']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class EditForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'firstName',
            'lastName',
            'email'
        )
