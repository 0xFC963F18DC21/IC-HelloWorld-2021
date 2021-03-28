from django.contrib import admin
from .models import AppUser
from .models import MyUser, FriendRequest


admin.site.register(AppUser)
admin.site.register(MyUser)
admin.site.register(FriendRequest)
