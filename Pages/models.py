from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext as _
from Blog.validators import validate_file_size
from django.contrib.auth.models import User
from io import BytesIO
from django.core.files import File
from PIL import Image
import uuid
from django.urls import reverse
# Create your models here.
class AboutUsPage(models.Model):
    """Model definition for About."""

    # TODO: Define fields here
    about = RichTextUploadingField()
    created=models.DateTimeField( auto_now_add=True)

    class Meta:
        """Meta definition for About."""

        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    # def __str__(self):
    #     """Unicode representation of About."""
    #     self.about
def compress_profile(profile):
    im = Image.open(profile)
    im_io = BytesIO()
    im = im.resize((250,250),Image.ANTIALIAS)
    im.save(im_io,'JPEG',quality =70)
    new_image=File(im_io,name=profile.name)
    return new_image
    
class Team(models.Model):
    """Model definition for Team."""

    # TODO: Define fields here
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    slug = models.UUIDField(default=uuid.uuid4, editable=False)
    fname = models.CharField(_("Firstname"), max_length=50)
    lname =models.CharField(_("Lastname"), max_length=50)
    bio = RichTextUploadingField(null=True)
    role = models.CharField(_("Role"), max_length=50)
    profile = models.ImageField(
        _("Profile Picture"),
        upload_to="user/team/profile",
        # height_field=None,
        # width_field=None,
        # max_length=None,
        
        validators=[validate_file_size]
    )
    twitter = models.URLField(_("Twitter"), max_length=200 )
    facebook = models.URLField(_("Facebook"), max_length=200)
    instagram = models.URLField(_("Instagram"), max_length=200)
    email = models.EmailField(_("Email"), max_length=254)
    created = models.DateTimeField( auto_now_add=True)
    
    class Meta:
        """Meta definition for Team."""

        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        """Unicode representation of Team."""
        return self.fname

    def save(self,*args, **kwargs):
        """Save method for Team."""
        new_profile = compress_profile(self.profile)
        self.profile= new_profile
        super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     """Return absolute url for Team."""
    #     return ('')

    # TODO: Define custom methods here
def compress(image):
    im = Image.open(image)
    im_io = BytesIO()
    im = im.resize((250,250),Image.ANTIALIAS)
    im.save(im_io,'JPEG',quality =70)
    new_image=File(im_io,name=image.name)
    return new_image

class Work(models.Model):
    """Model definition for Work."""

    # TODO: Define fields here
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    title = models.CharField(_("Title"), max_length=50)
    content = models.TextField(_("Content"))
    image = models.ImageField(_("Image"), upload_to='pages/what_we_do', validators=[validate_file_size] )
    created = models.DateTimeField( auto_now_add=True)
    class Meta:
        """Meta definition for Work."""

        verbose_name = 'Work'
        verbose_name_plural = 'Works'

    def __str__(self):
        """Unicode representation of Work."""
        return self.title

    def save(self,*args, **kwargs):
        """Save method for Work."""
        new_image = compress(self.image)
        self.image= new_image
        super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     """Return absolute url for Work."""
    #     return ('')

    # TODO: Define custom methods here

class Contact(models.Model):
    """Model definition for Contact."""

    # TODO: Define fields here
    name = models.CharField(_("Name"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    subject = models.CharField(_("Subject"), max_length=50)
    message = models.TextField(_("Description"))
    created = models.DateTimeField( auto_now_add=True)

    class Meta:
        """Meta definition for Contact."""

        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        """Unicode representation of Contact."""
        return self.name

    # def save(self):
    #     """Save method for Contact."""
    #     pass

    def get_absolute_url(self):
        """Return absolute url for Contact."""
        return reverse('contact')

    # TODO: Define custom methods here
