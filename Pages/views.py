from django.shortcuts import render
from .models import Team,Work,AboutUsPage,Contact
from django.views.generic import ListView,CreateView
from .forms import ContactForm
# Create your views here.

class About(ListView):
    model = AboutUsPage
    template_name = "pages/about.html"
    def get_context_data(self, **kwargs):
        context = super(About,self).get_context_data(**kwargs)
        # AboutUsPage_us= AboutUsPage.objects.all()
        context["aboutus"] = AboutUsPage.objects.all()
        context["works"] = Work.objects.all()
        context["teams"] = Team.objects.all()
        return context

class ContactCreateView(CreateView):
    model = Contact
    template_name = "pages/contact.html"
    form_class = ContactForm
    
    def form_valid(self,form):
     form.send()
     return super().form_valid(form)
