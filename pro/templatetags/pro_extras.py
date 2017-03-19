from django import template
from friend.models import Friend, AddFriend
from user.models import InfoWork
from status.models import Status
from django.db.models import Q

register = template.Library()

@register.filter
def render_friend_button(request_user, other_person):
    if request_user == other_person:
        return 'self'
    try:
        a = Friend.objects.get(user = request_user, friend = other_person)
        return 'friend'
    except Friend.DoesNotExist:
        try: 
            a = AddFriend.objects.get(inviter = request_user, receiver = other_person)
            if a.is_friend == True:
                return 'friend'
            return 'decline'
        except AddFriend.DoesNotExist:
            try:
                a = AddFriend.objects.get(inviter = other_person, receiver = request_user)
                if a.is_friend == True:
                    return 'friend'
                return 'refuse'
            except AddFriend.DoesNotExist:
                return 'stranger'

@register.filter
def filter_status(request_user, owner_user):
    if request_user == owner_user:
        return Status.objects.filter(user = request_user)
    else:
        t = Friend.objects.filter(user = owner_user)
        for i in t:
            if request_user == i.friend:
                return Status.objects.filter(Q(user = owner_user), Q(privacy = 'public') | Q(privacy = 'friend'))
        return Status.objects.filter(user = owner_user, privacy = 'public')

@register.filter
def is_friend(request_user, owner_user):
    f = Friend.objects.filter(user = request_user)
    is_friend = False
    for i in f:
        if i.friend == owner_user:
            is_friend = True
            break
    return is_friend
