from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify


class AppUser(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    username = models.TextField()
    spotify_access_token = models.TextField(blank=True, null=True)


class User(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    username = models.TextField()
    slug = models.SlugField(unique=True, max_length=255)

    spotify_auth_token = models.TextField(blank=True, null=True)
    spotify_refresh_token = models.TextField()
    spotify_access_token = models.TextField(blank=True, null=True)

    time_of_creation = models.DateTimeField()
    password_hash = models.TextField()  # Don't forget to add salt

    friends = models.ManyToManyField("User", blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(User, self).save(*args, **kwargs)


class FriendRequest(models.Model):
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='to_user', on_delete=models.CASCADE)
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='from_user', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "From {}, to {}".format(self.from_user.username, self.to_user.username)
