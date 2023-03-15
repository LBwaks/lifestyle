import uuid
from io import BytesIO

from django.contrib.auth.models import User
from django.core.files import File
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from PIL import Image
from Blog.validators import validate_file_size

# Create your models here.
my_gender = [
    ("Male", "Male"),
    ("Female", "Female"),
    ("Prefer not to say", "Prefer not to say"),
]

# compress profile image
def compress(profile):
    im = Image.open(profile)
    im_io = BytesIO()
    im = im.resize((150, 150),Image.ANTIALIAS)
    im.save(im_io, "JPEG", quality=70)
    # im_io.seek(0)
    new_image = File(im_io, name=profile.name)
    return new_image


class Profile(models.Model):
    """Model definition for Profile."""

    # TODO: Define fields here
    user = models.OneToOneField(
        User, related_name="user_profile", on_delete=models.CASCADE
    )
    firstname = models.CharField(_("Firstname"), max_length=50)
    lastname = models.CharField(_("Lastname"), max_length=50)
    slug = models.UUIDField(default=uuid.uuid4, editable=False)
    tell = models.CharField(_("Phone Number"), max_length=50, null=True, blank=True)
    gender = models.CharField(_("Gender"), choices=my_gender, max_length=50)
    dob = models.DateTimeField(_("Date Of Birth"), auto_now=False, auto_now_add=False)
    location = models.CharField(_("Location"), max_length=50, null=True, blank=True)
    bio = models.TextField(_("Bio"))
    profile = models.ImageField(
        _("Profile Picture"),
        upload_to="user/profiles",
        # height_field=None,
        # width_field=None,
        # max_length=None,
        null=True,
        blank=True,
        validators=[validate_file_size]
    )
    twitter = models.URLField(_("Twitter"), max_length=200)
    facebook = models.URLField(_("Facebook"), max_length=200)
    instagram = models.URLField(_("Instagram"), max_length=200)
    website = models.URLField(_("Website"), max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Profile."""

        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        """Unicode representation of Profile."""
        return str(self.firstname) + " " + str(self.lastname)

    def save(self,*args, **kwargs):
        """Save method for Profile."""
        new_profile = compress(self.profile)
        self.profile = new_profile
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Profile."""
        return reverse("user-profile", kwargs={"slug":self.slug})
        

    @property
    def profile_url(self):
        if self.profile and hasattr(self.profile, "url"):
            return self.profile.url

    # TODO: Define custom methods here
