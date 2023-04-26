from django.conf import settings
from django.core.mail import (
    BadHeaderError,
    EmailMessage,
    EmailMultiAlternatives,
    send_mail,
)
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import Context
from django.template.loader import render_to_string
from django.views.generic import CreateView, DetailView, ListView, TemplateView
from hitcount.views import HitCountDetailView

from Blog.models import Blog

from .forms import ContactForm
from .models import AboutUsPage, Contact, Team, Work

# Create your views here.


class Home(TemplateView):
    template_name = "pages/home.html"
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["featured_blogs"] = Blog.objects.prefetch_related('tags').select_related('category','user').filter(is_featured=True).order_by(
            "-created"
        )[:4]
        context["popular_blogs"] = Blog.objects.prefetch_related('tags').select_related('category','user').order_by("-hit_count_generic__hits")[:4]
        context["works"] = Work.objects.order_by("-created")
        return context


class About(ListView):
    model = AboutUsPage
    template_name = "pages/about.html"

    def get_context_data(self, **kwargs):
        context = super(About, self).get_context_data(**kwargs)
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
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            from_emaill = form.cleaned_data.get("email")
            subject = form.cleaned_data.get("subject")
            message = f"{name} with email {from_emaill} said:"
            message += f'\n Subject: "{subject}"\n\n'
            message += form.cleaned_data.get("message")

            context = {
                "name": name,
                "email": from_emaill,
                "subject": subject,
                "message": message,
            }
            text_content = render_to_string("email/contact-email.txt", context)
            html_content = render_to_string("email/contact-email.txt", context)

            try:
                mail = EmailMultiAlternatives(
                    subject=subject,
                    body=message,
                    from_email=from_emaill,
                    to=["obwakuvictor@gmail.com"],
                )
                mail.attach_alternative(html_content, "text/html")
                # mail.send(fail_silently=False)
                # send_mail(subject,message,from_emaill,[settings.RECIPIENT_ADDRESS])
                #  if send_mail(
                #     "subject",
                #     "with gmail",
                #     "obwakuvictor@gmail.com",
                #     ["victorobwaku@gmail.com"],
                # ):
               
                #     print('mail sent')
            except BadHeaderError:
                return HttpResponse("Invalid Header Found")
            return redirect("contact")

    return render(request, "pages/contact.html", {"form": form})
