from django import forms 
from .models import Contact
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.core.mail import send_mail
from django.conf import settings
class ContactForm(forms.ModelForm):
    """Form definition for Contact."""

    class Meta:
        """Meta definition for Contactform."""

        model = Contact
        fields = ('name','email','subject','message',)
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control name' 'required'}),
            'email':forms.EmailInput(attrs={'class':'form-control email''required'}),
            'message':forms.Textarea(attrs={'class':'form-control message' 'required'}),
            'subject':forms.TextInput(attrs={'class':'form-control subject' 'required'})
        }
    def get_info(self):
            cleaned_data = super(ContactForm,self).clean()
            name = cleaned_data.get('name')
            email = cleaned_data.get('email')
            subject = cleaned_data.get('subject')
            message =f'{name} with email {email} said:'
            message += f'\n Subject: {subject}\n\n'
            message += cleaned_data.get('message')

            return name, subject,message,email
    def send(self):
        subject,email,message =self.get_info()
        send_mail(
            subject=subject,
            message = message,
            from_email=email,
            recipient_list =[settings.RECIPIENT_ADDRESS]
        )
            
    def clean_name(self):
            name = self.cleaned_data['name']
            if len(name) < 3:
                raise ValidationError( _("Name should be more than 3 characters"), code="invalid")
            return name
        
    def clean_message(self):
            message = self.cleaned_data['message']
            if len(message) < 10 :
                raise ValidationError( _("Message should be more than 10 characters"), code="invalid")
            return message
    def clean_content(self):
            content = self.cleaned_data['content']
            if len(content) < 10:
                raise ValidationError( _("cDescription should be more than 10 characters"), code="invalid")
            return content