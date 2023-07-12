from django import template
from apps.blogs.models import Blog

register = template.Library()


@register.simple_tag()
def latest_three_blogs():
    return Blog.objects.order_by('-id')[:3]
