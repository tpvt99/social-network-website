from django import template
from friend.models import AddFriend, Friend
register = template.Library()

@register.filter
def friend(user, who):
    try:
        a = Friend.objects.get(user= user, friend = who)
        return 'friend'
    except Friend.DoesNotExist:
        try:
            t = AddFriend.objects.get(inviter = user, receiver = who, is_friend = False)
            return 'decline'
        except AddFriend.DoesNotExist:
            try:
                t = AddFriend.objects.get(inviter = who, receiver = user, is_friend = False)
                return 'accept'
            except AddFriend.DoesNotExist:
                return 'connect'

