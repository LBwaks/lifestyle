from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from taggit.forms import *
from taggit.models import Tag

from .models import Blog, Comment


class BlogForm(forms.ModelForm):
    """Form definition for Blog.""" 
    # class="form-select form-select-sm" id="small-bootstrap-class-single-field"

    tags = forms.ModelMultipleChoiceField(label="Tags", widget=forms.SelectMultiple(attrs={"class":"form-select  w-100 form-control tag-multiple" ,"style":"width:100%" ,"multiple":'multiple'}),queryset=Tag.objects.all())
    # tags = forms.ModelMultipleChoiceField(label="Tags", widget=forms.SelectMultiple(attrs={"class":"form-select form-select-sm" ,"id":"small-bootstrap-class-single-field" ,"multiple":'multiple'}),queryset=Tag.objects.all())
    content = (forms.CharField(widget=CKEditorUploadingWidget()),)

    class Meta:
        """Meta definition for Blogform."""

        model = Blog
        fields = (
            "title",
            "category",
            "tags",
            "content",            
            "photo",
        )
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control title" "required"}),
            "category": forms.Select(
                attrs={"class": "form-control category" "required"}
            ),
            "photo": forms.ClearableFileInput(attrs={"class": "form-control","accept":".png,.jpg,.jpeg"}),
        }

    def clean_title(self):
        title = self.cleaned_data["title"]
        if len(title) <= 5:
            raise ValidationError(
                _("Title should be more than 5 Characters"), code="invalid"
            )
        return title

    def clean_content(self):
        content = self.cleaned_data["content"]
        if len(content) <= 100:
            raise ValidationError(
                _("Characters should be more than 100"), code="invalid"
            )
        return content

    def clean_photo(self):
        photo = self.cleaned_data.get("photo", False)
        if photo:
            if photo.size > 5*1024*1024:
                raise ValidationError(
                    _("Photo should be less than 5mbs"), code="invalid"
                )

        return photo


class EditBlogForm(forms.ModelForm):
    """Form definition for Blog."""

    tags = forms.ModelMultipleChoiceField(label="Tags", widget=forms.SelectMultiple(attrs={"class":"form-select form-select-sm" ,"id":"small-bootstrap-class-single-field" ,"multiple":'multiple'}),queryset=Tag.objects.all())
    content = (forms.CharField(widget=CKEditorUploadingWidget()),)

    class Meta:
        """Meta definition for Blogform."""

        model = Blog
        fields = (
            "title",
            "content",
            "category",
            "tags",
            "photo",
        )
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control title" "required"}),
            "category": forms.Select(
                attrs={"class": "form-control category" "required"}
            ),
            "photo": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }

    def clean_title(self):
            title = self.cleaned_data["title"]
            if len(title) <= 5:
                raise ValidationError(
                    _("Title should be more than 5 Characters"), code="invalid"
                )
            return title

    def clean_content(self):
            content = self.cleaned_data["content"]
            if len(content) <= 100:
                raise ValidationError(
                    _("Characters should be more than 100"), code="invalid"
                )
            return content

    def clean_photo(self):
        photo = self.cleaned_data.get("photo", False)
        if photo:
            if photo.size > 5*1024*1024:
                raise ValidationError(
                    _("Photo should be less than 5mbs"), code="invalid"
                )

        return photo


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            "comment",
            "parent",
        )
        widgets = {
            "comment": forms.Textarea(
                attrs={"class": "form-control comment" "required"}
            ),
            'parent': forms.HiddenInput()
        }
