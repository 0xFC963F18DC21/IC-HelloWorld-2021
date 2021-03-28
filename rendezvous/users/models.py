from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class AppUser(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    username = models.CharField(max_length=120)
    spotify_access_token = models.TextField(blank=True, null=True)


class MyUser(models.Model):
    ## User field here is to connect our own model to django's own user model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, max_length=255)

    spotify_auth_token = models.TextField(blank=True, null=True)
    spotify_refresh_token = models.TextField(blank=True, null=True)
    spotify_access_token = models.TextField(blank=True, null=True)

    friends = models.ManyToManyField("MyUser", blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user) #slug won't work
        super(MyUser, self).save(*args, **kwargs)

@receiver(post_save, sender=User)
def create_user_myUser(sender, instance, created, **kwargs):
    if created:
        MyUser.objects.create(user=instance)

class FriendRequest(models.Model):
    to_user = models.ForeignKey(MyUser, related_name='to_user', on_delete=models.CASCADE)
    from_user = models.ForeignKey(MyUser, related_name='from_user', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "From {}, to {}".format(self.from_user.username, self.to_user.username)
