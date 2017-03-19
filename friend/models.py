from django.db import models
from django.conf import settings

# Create your models here.

class Friend(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")
    friend = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_friend")
    friend_since = models.DateTimeField(auto_now_add = True)

    class Meta:
        unique_together = ('user','friend')

class AddFriend(models.Model):
    inviter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE,related_name = "%(app_label)s_%(class)s_inviter")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_receiver")
    invite_time = models.DateTimeField(auto_now_add = True)
    is_friend = models.BooleanField(default = False)
    read = models.BooleanField(default = False)

    class Meta:
        unique_together = ("inviter", "receiver")
