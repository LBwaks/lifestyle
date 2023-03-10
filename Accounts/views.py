from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, UpdateView

from .forms import UpdateProfileForm
from .models import Profile

# Create your views here.


class UserProfileView(TemplateView):
    template_name = "profiles/profile.html"

    def get_context_data(self, slug, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context["profile"] = get_object_or_404(Profile, slug=slug)
        return context

class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = "profiles/update-profile.html"
    form_class = UpdateProfileForm

