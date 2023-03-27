from io import BytesIO

from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.core.files import File
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django_extensions.db.fields import AutoSlugField
from hitcount.models import HitCount, HitCountMixin
from PIL import Image
from django.contrib.postgres.search import SearchVectorField
from taggit.managers import TaggableManager
from .managers import CategoryManager, BlogManager
from .validators import validate_file_size
from django.contrib.postgres.indexes import GinIndex
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
    is_published = models.BooleanField(default=True)
    objects = models.Manager()
    publishedCategory =CategoryManager()
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


# compress profile image
def compress(photo):
    im = Image.open(photo)
    im_io = BytesIO()
    im = im.resize((800, 432), Image.ANTIALIAS)
    im.save(im_io, "JPEG", quality=70)
    # im_io.seek(0)
    new_image = File(im_io, name=photo.name)
    return new_image


# Create your models here.
class Blog(models.Model, HitCountMixin):
    """Model definition for Blog."""

    # TODO: Define fields here
    user = models.ForeignKey(
        User, verbose_name=_("blog_author"), on_delete=models.CASCADE
    )
    title = models.CharField(_("Title"), max_length=50)
    slug = AutoSlugField(populate_from="title", slugify_function=my_slugify_function)
    content = RichTextUploadingField(_("Content"))
    category = models.ForeignKey(
        "Category", verbose_name=_("blog_category"), on_delete=models.CASCADE
    )
    tags = TaggableManager(_("Tags"))
    photo = models.ImageField(
        _("Photo"),
        upload_to="images/blog",
        blank=True,
        null=True,
        height_field=None,
        width_field=None,
        max_length=None,
        validators=[validate_file_size],
        
    )

    hit_count_generic = GenericRelation(
        HitCount,
        object_id_field="object_pk",
        related_query_name="hit_count_generic_relation",
    )
    objects = models.Manager()
    publishedBlogs = BlogManager()
    # search_vector = SearchVectorField(null=True)
    bookmarks = models.ManyToManyField(User, related_name='bookmarks', default=None, blank=True)
    is_published = models.BooleanField(_("Is Published"), default=True)
    is_featured = models.BooleanField(_("Is Featured"), default=False)
    updated = models.DateTimeField(_("Updated"), auto_now=True, auto_now_add=False)
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        """Meta definition for Blog."""

        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        ordering = ("created",)
        # indexes =[
        #      GinIndex(name='NewGinIndex',fields=['title','content',],opclasses=['gin_trgm_ops','gin_trgm_ops'])
        # ]

    def __str__(self):
        """Unicode representation of Blog."""
        return self.title

    def save(self, *args, **kwargs):
        """Save method for photo."""
        new_photo = compress(self.photo)
        self.photo = new_photo
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Blog."""
        return reverse("blog-detail", kwargs={"slug": self.slug})

    def get_read_time(self):
        from html import unescape

        from django.utils.html import strip_tags

        string = self.title + unescape(strip_tags(self.content))
        total_words = len((string).split())
        return round(total_words / 265)

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, "url"):
            return self.photo.url

    # TODO: Define custom methods here


class Comment(models.Model):
    """Model definition for Comment."""

    # TODO: Define fields here
    blog = models.ForeignKey(
        Blog,
        verbose_name=_("blog_comment"),
        related_name="comments",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User, verbose_name=_("blog_user"), on_delete=models.CASCADE
    )
    comment = models.TextField(_("Comment"))
    created = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        "self", related_name="replies", null=True, blank=True, on_delete=models.CASCADE
    )

    class Meta:
        """Meta definition for Comment."""

        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ["-created"]

    def __str__(self):
        """Unicode representation of Comment."""
        return str(self.user) + " says " + str(self.comment)

    # def save(self):
    #     """Save method for Comment."""
    #     pass

    def get_absolute_url(self):
        """Return absolute url for Comment."""
        return ""

    @property
    def children(self):
        return Comment.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False

    # TODO: Define custom methods here
