from django.db import models


class AppUser(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    username = models.TextField()
    spotify_access_token = models.TextField(blank=True, null=True)


class User(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    username = models.TextField()

    spotify_auth_token = models.TextField(blank=True, null=True)
    spotify_refresh_token = models.TextField()
    spotify_access_token = models.TextField(blank=True, null=True)

    time_of_creation = models.DateTimeField()

    friends = models.ManyToManyField("User", blank=True)
