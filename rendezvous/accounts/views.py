from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect
from ..accounts.forms import RegisterForm, EditForm
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            userName = request.POST.get('username')
            passWord = request.POST.get('password1')
            user = authenticate(request, userName=userName, passWord=passWord)
            login(request, user)
            return redirect(reverse('home:home'))

    else:
        form = RegisterForm()

    content = {'form': form}
    return render(request, 'accounts/regForm.html', content)


@login_required()
def viewProfile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user

    content = {'user': user}
    return render(request, 'accounts/profile.html', content)


@login_required()
def editProfile(request):
    if request.method == 'POST':
        form = EditForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:viewProfile'))

    else:
        form = EditForm(instance=request.user)
        content = {'form': form}
        return render(request, 'accounts/edit_profile.html', content)


@login_required()
def passWordChange(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user)
        content = {'form': form}
        return render(request, 'accounts/change_password.html', content)
