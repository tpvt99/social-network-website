from django import template
register = template.Library()

@register.filter
def message_buddy(request_user, chat_buddy):
    if len(chat_buddy) == 2:
        for i in chat_buddy:
            if i != request_user:
                return i

@register.filter
def last_message(chat_buddy):
    t = chat_buddy.message_message_chat_buddies.all().order_by('-create_time')[0]
    return t
