
from django import template
from Blog.models import Blog
register =template.Library()

@register.simple_tag
def popular_blogs():
    # blogs = Blog.objects.filter('-created')[:5]
    # return {'resent_blogs':blogs}
    return Blog.objects.order_by("-hit_count_generic__hits")[:5]
