from django.db import models
from django.conf import settings

# Create your models here.

from activities.models import Activity
from plan.models import Plan

class PlayFriend(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE, null = True)
    plan = models.ForeignKey(Plan, on_delete = models.CASCADE, null = True)

class Sport(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE, null = True)
    plan = models.ForeignKey(Plan, on_delete = models.CASCADE, null = True)
