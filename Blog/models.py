from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _
from django_extensions.db.fields import AutoSlugField
from hitcount.models import HitCountMixin
from taggit.managers import TaggableManager

# Create your models here.


def my_slugify_function(content):
    return content.replace("_", "-").lower()


class Category(models.Model):
    """Model definition for Category."""

    # TODO: Define fields here

    user = models.ForeignKey(
        User,
        related_name="events_category",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=50, unique=True)
    slug = AutoSlugField(populate_from="name", slugify_function=my_slugify_function)
    description = models.TextField(max_length=250)
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Category."""

        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        """Unicode representation of Category."""
        return self.name

    # def save(self):
    #     """Save method for Category."""
    #     pass

    # def get_absolute_url(self):
    #     """Return absolute url for Category."""
    #     return ""

    # # TODO: Define custom methods here


# Create your models here.
class Blog(models.Model):
    """Model definition for Blog."""

    # TODO: Define fields here
    user = models.ForeignKey(
        User, verbose_name=_("blog_author"), on_delete=models.CASCADE
    )
    title = models.CharField(_("Title"), max_length=50)
    slug = AutoSlugField(populate_from="title", slugify_function=my_slugify_function)
    content = RichTextField(_("Content"))
    category = models.ForeignKey(
        "Category", verbose_name=_("blog_category"), on_delete=models.CASCADE
    )
    tags = TaggableManager(_("Tags"))
    photo = models.ImageField(
        _("Photo"),
        upload_to="images/blog",
        height_field=None,
        width_field=None,
        max_length=None,
    )
    # hit_count_generic = GenericRelation(
    # HitCount, object_id_field='object_pk',
    # related_query_name='hit_count_generic_relation')
    reference = models.URLField(_("Reference"), max_length=200)
    is_published = models.BooleanField(_("Is Published"), default=False)
    is_featured = models.BooleanField(_("Is Featured"), default=False)
    updated = models.DateTimeField(_("Updated"), auto_now=True, auto_now_add=False)
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        """Meta definition for Blog."""

        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        ordering = ("created",)

    def __str__(self):
        """Unicode representation of Blog."""
        return self.title

    # def save(self):
    #     """Save method for Blog."""
    #     pass

    # def get_absolute_url(self):
    #     """Return absolute url for Blog."""
    #     return ""

    # TODO: Define custom methods here
