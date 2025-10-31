from django import template
from urllib.parse import urlencode

register = template.Library()

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    query = context['request'].GET.copy()
    for k, v in kwargs.items():
        if v is None:
            query.pop(k, None)
        else:
            query[k] = v
    encoded = query.urlencode()
    return f'?{encoded}' if encoded else '?'
