from django.http import JsonResponse

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.conf import settings
from django.http import HttpResponseRedirect
from .models import User, FriendRequest
from .forms import UserRegisterForm
import random

User = User


@login_required
def friend_list(request):
    p = request.user.profile
    friends = p.friends.all()
    context = {
        'friends': friends
    }
    return render(request, "users/friend_list.html", context)


def Callback(request):
    # Save code to current user object
    return JsonResponse(request.GET.get('code', ''), safe=False)
