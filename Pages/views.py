from django.shortcuts import render
from .models import Team,Work,AboutUsPage,Contact
from django.views.generic import ListView,CreateView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf import settings
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

# class ContactCreateView(CreateView):
#     model = Contact
#     template_name = "pages/contact.html"
#     form_class = ContactForm
   

#     def form_valid(self,form):
            
#       form.send()
    #   return super().form_valid(form)
def ContactView(request):
    if request.method =="GET":
        form=ContactForm
    else:
        form =ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            from_email = form.cleaned_data.get('email')
            subject =form.cleaned_data.get('subject')
            message =f'{name} with email {from_email} said:'
            message += f'\n Subject: "{subject}"\n\n'
            message += form.cleaned_data.get('message')
            try:
                send_mail(subject,message,from_email,[settings.RECIPIENT_ADDRESS])
            except BadHeaderError:
                return HttpResponse('Invalid Header Found')
            return redirect('contact')
            
    return render(request ,"pages/contact.html",{'form':form})