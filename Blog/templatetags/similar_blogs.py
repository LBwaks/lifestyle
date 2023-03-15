from django import template 
from Blog.models import Blog
register =template.Library()

@register.simple_tag
def similar():
    pass