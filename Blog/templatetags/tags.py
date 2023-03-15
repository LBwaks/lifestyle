from django import template
from taggit.models import Tag
register = template.Library()

@register.simple_tag
def tags():
    
    return Tag.objects.all()
    