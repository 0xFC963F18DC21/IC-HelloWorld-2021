from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify


class AppUser(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    username = models.CharField(max_length=120)
    spotify_access_token = models.TextField(blank=True, null=True)


class MyUser(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    username = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, max_length=255)

    spotify_auth_token = models.TextField(blank=True, null=True)
    spotify_refresh_token = models.TextField(blank=True, null=True)
    spotify_access_token = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=120)  # Don't forget to add salt

    friends = models.ManyToManyField("MyUser", blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super(MyUser, self).save(*args, **kwargs)


class FriendRequest(models.Model):
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='to_user', on_delete=models.CASCADE)
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='from_user', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "From {}, to {}".format(self.from_user.username, self.to_user.username)
