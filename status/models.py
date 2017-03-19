from django.db import models
from django.conf import settings

from act.models import Act, ActPost
from activity.models import Activity, ActivityPost
from activities.models import ActivitiesPost
from event.models import Event, EventPost
from post.models import Post
from events.models import EventsPost
from contest.models import Contest, ContestPost
from trait.models import Trait

# Create your models here.

class Status(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user", null = True)
    time_create = models.DateTimeField(auto_now_add = True)
    status_type = models.CharField(max_length = 100)
    act = models.ForeignKey(Act, on_delete = models.CASCADE, null = True)
    actpost = models.ForeignKey(ActPost, on_delete = models.CASCADE, null = True)
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE, null = True)
    activitypost = models.ForeignKey(ActivityPost, on_delete = models.CASCADE, null = True)
    activitiespost= models.ForeignKey(ActivitiesPost, on_delete = models.CASCADE, null = True)
    event = models.ForeignKey(Event, on_delete = models.CASCADE, null = True)
    eventpost = models.ForeignKey(EventPost, on_delete = models.CASCADE, null = True)
    eventspost = models.ForeignKey(EventsPost, on_delete = models.CASCADE ,null = True)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, null = True)
    contest = models.ForeignKey(Contest, on_delete = models.CASCADE, null = True)
    contestpost = models.ForeignKey(ContestPost, on_delete = models.CASCADE, null = True)
    trait = models.ForeignKey(Trait, on_delete = models.CASCADE, null = True)
    privacy = models.CharField(max_length = 100, null = True)
    vote = models.IntegerField(default = 0)

class StatusVote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")
    status = models.ForeignKey(Status, on_delete = models.CASCADE)
    been_vote = models.BooleanField(default = False)
    time_create = models.DateTimeField(auto_now_add = True)

    class Meta:
        unique_together = ('user','status')

class StatusComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")
    status = models.ForeignKey(Status, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_status")
    comment = models.CharField(max_length = 200)
    time_create = models.DateTimeField(auto_now_add = True)
