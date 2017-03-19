from django import template
register = template.Library()

from status.models import StatusVote
from status.models import Status
from friend.models import Friend
import math

@register.filter
def render_cool(user, status):
    try:
        s = StatusVote.objects.get(user = user, status = status)
        if s.been_vote == True:
            return True
        return False
    except StatusVote.DoesNotExist:
        return False

@register.filter
def render_cool_percentage(post_id):
    t = Status.objects.get(pk__exact = int(post_id))
    total_friend = len(Friend.objects.filter(user = t.user))
    total_vote = len(StatusVote.objects.filter(status = t, been_vote = True))
    max_percent = math.floor(0.1 * total_friend)
    if max_percent == 0:
        max_percent = 1
    percent = math.ceil(total_vote/max_percent * 100)
    if percent > 100:
        percent = 100
    return percent

@register.filter
def mul(num, factor):
    return math.ceil(num * factor)
