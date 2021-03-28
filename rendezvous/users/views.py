from django.http import JsonResponse

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import MyUser, FriendRequest
from .forms import UserRegisterForm, UserLoginForm
import random

User = MyUser


def friend_list(request):
    p = request.user
    friends = p.friends.all()
    context = {
        'friends': friends
    }
    return render(request, "users/friend_list.html", context)


@login_required
def send_friend_request(request, searchId):
    user = get_object_or_404(MyUser, id=searchId)
    frequest, created = FriendRequest.objects.get_or_create(
        from_user=request.user,
        to_user=user)
    return HttpResponseRedirect('/users/{}'.format(user.slug))


@login_required
def accept_friend_request(request, searchId):
    from_user = get_object_or_404(MyUser, id=searchId)
    frequest = FriendRequest.objects.filter(from_user=from_user, to_user=request.user).first()
    user1 = frequest.to_user
    user2 = from_user
    user1.friends.add(user2.profile)
    user2.friends.add(user1.profile)
    if FriendRequest.objects.filter(from_user=request.user, to_user=from_user).first():
        request_rev = FriendRequest.objects.filter(from_user=request.user, to_user=from_user).first()
        request_rev.delete()
    frequest.delete()
    return HttpResponseRedirect('/users/{}'.format(request.user.slug))


@login_required
def profile_view(request, slug):
    p = MyUser.objects.filter(slug=slug).first()
    u = p
    sent_friend_requests = FriendRequest.objects.filter(from_user=p.user)
    rec_friend_requests = FriendRequest.objects.filter(to_user=p.user)

    friends = p.friends.all()

    # is this user our friend
    button_status = 'none'
    if p not in request.user.profile.friends.all():
        button_status = 'not_friend'

        # if we have sent him a friend request
        if len(FriendRequest.objects.filter(
                from_user=request.user).filter(to_user=p.user)) == 1:
            button_status = 'friend_request_sent'

        # if we have recieved a friend request
        if len(FriendRequest.objects.filter(
                from_user=p.user).filter(to_user=request.user)) == 1:
            button_status = 'friend_request_received'

    context = {
        'u': u,
        'button_status': button_status,
        'friends_list': friends,
        'sent_friend_requests': sent_friend_requests,
        'rec_friend_requests': rec_friend_requests,
    }

    return render(request, "profile.html", context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():

                print(User.objects.filter(username=form.cleaned_data['username']))
                return render(request, 'register.html', {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            else:
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Your account ({username}) has been created! You can now login!')
                return redirect('/login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            possibleUsers = User.objects.filter(username=username)
            print([person.password for person in possibleUsers])
            if len(possibleUsers.filter(password=password)) >= 1:
                print(request.user)
                messages.success(request, f'Your account has been logged in to! You can now login!')
                return redirect(reverse('profile'))
            return render(request, 'login.html', {
                'form': form,
                'error_message': 'Invalid username or password'
            })
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def my_profile(request):
    p = request.user
    myUserP = MyUser.objects.filter(user=p)
    you = myUserP
    sent_friend_requests = FriendRequest.objects.filter(from_user=you)
    rec_friend_requests = FriendRequest.objects.filter(to_user=you)
    friends = myUserP.friends

    # is this user our friend
    button_status = 'none'
    if myUserP not in myUserP.objects.all():
        button_status = 'not_friend'

        # if we have sent him a friend request
        if len(FriendRequest.objects.filter(
                from_user=myUserP).filter(to_user=you)) == 1:
            button_status = 'friend_request_sent'

        if len(FriendRequest.objects.filter(
                from_user=p.user).filter(to_user=request.user)) == 1:
            button_status = 'friend_request_received'

    context = {
        'u': you,
        'button_status': button_status,
        'friends_list': friends,
        'sent_friend_requests': sent_friend_requests,
        'rec_friend_requests': rec_friend_requests,
    }

    return render(request, "profile.html", context)


@login_required
def search_users(request):
    query = request.GET.get('q')
    object_list = MyUser.objects.filter(username__icontains=query)
    context = {
        'users': object_list
    }
    return render(request, "users/search_users.html", context)


def Callback(request):
    # Save code to current user object
    return JsonResponse(request.GET.get('code', ''), safe=False)
