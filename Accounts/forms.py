from django import forms
from django.core.exceptions import ValidationError

from .models import Profile


class UpdateProfileForm(forms.ModelForm):
    """Form definition for Profile."""

    class Meta:
        """Meta definition for Profileform."""

        model = Profile
        fields = (
            "firstname",
            "lastname",
            "tell",
            "gender",
            "dob",
            "location",
            "bio",
            "profile",
            "twitter",
            "facebook",
            "instagram",
            "website",
        )
        widgets = {
            "firstname": forms.TextInput(
                attrs={"class": "form-control firstname" "required"}
            ),
            "lastname": forms.TextInput(
                attrs={"class": "form-control lastname" "required"}
            ),
            "tell": forms.TextInput(attrs={"class": "form-control tell"}),
            "gender": forms.Select(attrs={"class": "form-control" "required"}),
            "dob": forms.DateTimeInput(attrs={"class": "form-control dob" "required"}),
            "location": forms.TextInput(attrs={"class": "form-control location"}),
            "bio": forms.Textarea(attrs={"class": "form-control bio" "required"}),
            "profile": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "twitter": forms.URLInput(attrs={"class": "form-control twitter"}),
            "facebook": forms.URLInput(attrs={"class": "form-control facebook"}),
            "instagram": forms.URLInput(attrs={"class": "form-control instagram"}),
            "website": forms.URLInput(attrs={"class": "form-control website"}),
        }

    def clean_profile(self):
            data = self.cleaned_data.get("profile")
            if data:
                if data.size > 2 * 1024 * 1024:
                    raise ValidationError("Profile should be less than 5mbs")

            return data
# 