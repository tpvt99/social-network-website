from django.db import models
from django.conf import settings

# Create your models here.

def upload_group_pic(instace, filename):
    return 'group/{0}'.format(filename)

class Group(models.Model):
    admin = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = "%(app_label)s_%(class)s_admin")
    name = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = upload_group_pic)
    privacy = models.CharField(max_length = 100) #public, private
    time_create = models.DateTimeField(auto_now_add = True)
    group_type = models.CharField(max_length = 100, null = True)

class Member(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name="%(app_label)s_%(class)s_user")
    group = models.ForeignKey(Group, on_delete = models.CASCADE, related_name="%(app_label)s_%(class)s_group")
    group_type = models.CharField(max_length = 100) # social, work, entertainment
    join_time = models.DateTimeField(auto_now_add = True)

class GroupInvitation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name="%(app_label)s_%(class)s_user")
    who_invite = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name="%(app_label)s_%(class)s_who_invite")
    group = models.ForeignKey(Group, on_delete = models.CASCADE, related_name="%(app_label)s_%(class)s_group")
    time_invitation = models.DateTimeField(auto_now_add = True)
    is_member = models.BooleanField(default = False)

class GroupPost(models.Model):
    group = models.ForeignKey(Group, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_group")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name="%(app_label)s_%(class)s_user")
    text = models.TextField(max_length = 100)
