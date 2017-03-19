from django.db import models
from django.conf import settings

# Create your models here.

from activities.models import Activity

class ActivityVote(models.Model):
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE, related_name ="%(app_label)s_%(class)s_activity")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")
    been_vote = models.BooleanField(default = False)

    class Meta:
        unique_together = ('activity','user')
