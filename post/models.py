from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user", null = True)
    text = models.TextField()
    time_create = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to = 'media', null = True)
    privacy = models.CharField(max_length = 100)
    province = models.CharField(max_length = 200, null = True) #2
    province_unicode = models.CharField(max_length = 200, null = True) #2

class PostFriend(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    friend = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_friend")
