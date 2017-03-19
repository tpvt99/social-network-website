from django.db import models
from django.conf import settings

# Create your models here.

class MessageUser(models.Model):
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = "%(app_label)s_%(class)s_user")
    last_active = models.DateTimeField(null = True)
    read = models.BooleanField(default = False)

class Message(models.Model):
    user_send = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_usersend")
    chat_buddies = models.ForeignKey(MessageUser, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_chat_buddies")
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add = True)
    read = models.BooleanField(default = False)
