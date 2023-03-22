from django import template
from Blog.models import Category
register =template.Library()

@register.simple_tag
def category():
    # blogs = Blog.objects.filter('-created')[:5]
    # return {'resent_blogs':blogs}
    return Category.objects.all()