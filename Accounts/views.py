from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, UpdateView

from .forms import UpdateProfileForm
from .models import Profile
from Pages.models import Team
from Blog.models import Blog
from django.contrib.auth.models import User

# Create your views here.


class UserProfileView(TemplateView):
    template_name = "profiles/profile.html"

    def get_context_data(self, slug, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        profile = get_object_or_404(Profile, slug=slug)
        contributions = Blog.objects.filter(user = self.request.user).count()
        context["profile"] = profile
        context['contributions']= contributions
        print("this user contributions are:",contributions)
        return context
    
# class TeamProfileView(TemplateView):
#     template_name = "profiles/team_profile.html"
#     def get_context_data(self, slug, **kwargs):
#         context = super(TeamProfileView, self).get_context_data(**kwargs)
#         context["profile"] = get_object_or_404(Team, slug=slug)
#         return context
class BloggerDetailView(TemplateView):
    model = User
    template_name = "profiles/blogger_profile.html"
    def get_context_data(self, username, **kwargs):
        context = super(BloggerDetailView, self).get_context_data(**kwargs)
        user_profile = get_object_or_404(User, username=username)
        context["profile"] = get_object_or_404(Profile, user=user_profile.id)
        return context


class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = "profiles/update-profile.html"
    form_class = UpdateProfileForm

