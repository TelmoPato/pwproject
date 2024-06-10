from django import template

register = template.Library()

@register.filter(name='format_duration')
def format_duration(duration):
    minutes = duration // 60
    seconds = duration % 60
    return f"{minutes}:{seconds:02d}"
