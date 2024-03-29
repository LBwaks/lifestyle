import uuid
from io import BytesIO
from django.core.files.storage import default_storage
from django.contrib.auth.models import User
from django.core.files import File
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from Blog.validators import validate_file_size
from django.core.validators import FileExtensionValidator
# Create your models here.
ext_validator =FileExtensionValidator(['jpg','png','jpeg','gif'])
my_gender = [
    ("Male", "Male"),
    ("Female", "Female"),
    ("Prefer not to say", "Prefer not to say"),
]

# compress profile image
# def compress(profile):
#     im = Image.open(profile)
#     im_io = BytesIO()
#     im = im.resize((150, 150), Image.ANTIALIAS)
#     im.save(im_io, "JPEG", quality=70)
#     # im_io.seek(0)
#     new_image = File(im_io, name=profile.name)
#     return new_image


class Profile(models.Model):
    """Model definition for Profile."""

    # TODO: Define fields here
    user = models.OneToOneField(
        User, related_name="user_profile", on_delete=models.CASCADE
    )
    firstname = models.CharField(_("Firstname"), max_length=50,)
    lastname = models.CharField(_("Lastname"), max_length=50,)
    slug = models.UUIDField(default=uuid.uuid4, editable=False)
    tell = models.CharField(_("Phone Number"), max_length=50, null=True, blank=True)
    gender = models.CharField(_("Gender"), choices=my_gender, max_length=50,)
    dob = models.DateTimeField(_("Date Of Birth"), auto_now=False, auto_now_add=False,null=True, blank=True)
    location = models.CharField(_("Location"), max_length=50,)
    bio = models.TextField(_("Bio"))
    profile = models.ImageField(
        _("Profile Picture"),
        upload_to="profiles",
        # height_field=None,
        # width_field=None,
        # max_length=100,
        null=True,
        blank=True,
        # default="default_profile.png",
        validators=[validate_file_size,ext_validator],
    )
    twitter = models.URLField(
        _("Twitter"),
        max_length=200,
        null=True,
        blank=True,
    )
    facebook = models.URLField(
        _("Facebook"),
        max_length=200,
        null=True,
        blank=True,
    )
    instagram = models.URLField(
        _("Instagram"),
        max_length=200,
        null=True,
        blank=True,
    )
    website = models.URLField(
        _("Website"),
        max_length=200,
        null=True,
        blank=True,
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Profile."""

        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        """Unicode representation of Profile."""
        return str(self.firstname) + " " + str(self.lastname)

    # def save(self, *args, **kwargs):
    # #     """Save method for Profile."""
    # #     new_profile = compress(self.profile)
    # #     self.profile = new_profile
    #     # super().save(*args, **kwargs)
    #     super().save(*args, **kwargs)
    #     if self.profile:
    #         # with default_storage.open(self.profile.name, "rb") as file:
    #         #     img = Image.open(file)
    #             img = Image.open(self.profile.name)
    #             if img.height > 300 or img.width > 300:
    #                 output_size = (300, 300)
    #                 img.thumbnail(output_size)
    #                 # Create a new filename for the resized image
    #                 # Create a new filename for the resized image
    #                 # resized_filename = f"resized_{self.profile.name}"
    #                 # resized_filepath = default_storage.save(resized_filename, img)

    #                 # # Create a new ImageField instance with the resized image
    #                 # resized_profile = models.ImageField()
    #                 # resized_profile.name = resized_filepath

    #                 # # Update the profile field with the new instance
    #                 # self.profile = resized_profile
    #                 img.save(self.profile.path)
    #                 super().save(*args, **kwargs)


       
        # if self.pk is None:  # Only resize when the profile is being created
        #     if self.profile:  # Check if a profile picture is provided
        #         super().save(*args, **kwargs)  # Save the model instance first
        #         img = Image.open(self.profile.name)

        #         if img.height > 300 or img.width > 300:
        #             output_size = (300, 300)
        #             img.thumbnail(output_size)
        #             img.save(self.profile.path)
        # else:
        #     super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Profile."""
        return reverse("user-profile", kwargs={"slug": self.slug})

    @property
    def profile_url(self):
        if self.profile and hasattr(self.profile, "url"):
            return self.profile.url

    # TODO: Define custom methods here
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
@receiver(post_save,sender =User)
def save_profile(sender,instance ,**kwargs):
    instance.user_profile.save()
