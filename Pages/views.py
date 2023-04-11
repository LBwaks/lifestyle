from django.shortcuts import render
from .models import Team,Work,AboutUsPage,Contact
from django.views.generic import ListView,CreateView,TemplateView,DetailView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ContactForm
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template import Context
from django.template .loader import render_to_string
# Create your views here.


class Home(TemplateView):
    template_name = "pages/home.html"

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
            
            
            
            context ={
                'name':name,
                'email': from_email,
                'subject':subject,
                'message':message
            }
            text_content =render_to_string('email/contact-email.txt',context)
            html_content =render_to_string('email/contact-email.txt',context)
            
            
            try:
                mail =EmailMultiAlternatives(
                    subject= subject,
                    body=message,
                    from_email= from_email,
                    to=['obwakuvictor@gmail.com']
                    
                )
                mail.attach_alternative(html_content,"text/html")
                mail.send(fail_silently=False)
                # send_mail(subject,message,from_email,[settings.RECIPIENT_ADDRESS])
            except BadHeaderError:
                return HttpResponse('Invalid Header Found')
            return redirect('contact')
            
    return render(request ,"pages/contact.html",{'form':form})