from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()

@register.filter
@register.simple_tag
def highlight(text, search):
    search = re.split((" "), search)

    for i in search:
        highlighted = re.sub(i, '<span style="background-color: #000FF">{}</span>'.format(i), text, flags=re.IGNORECASE)
        text = highlighted
    return mark_safe(text)

