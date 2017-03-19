from django import template

register = template.Library()

@register.filter
def listitem(arg1, arg2):
    if type(arg1) == list and arg2 != '':
        arg2 = int(arg2)
        return arg1[arg2]
