from django.db import models


class AppUser(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    username = models.TextField()
    spotify_access_token = models.TextField(blank=True, null=True)
