from django import template

register = template.Library()

from trait.models import Trait

@register.filter
def trait(user):
    t = Trait.objects.filter(user_receive = user)
    result = {}
    for i in t:
        result[i.trait_type] = result.setdefault(i.trait_type,0) + 1
    return result
