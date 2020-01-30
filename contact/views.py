from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from models import Contact, ContactForm
from django.core.urlresolvers import reverse_lazy
from django.core.mail import get_connection
from django.core.mail.message import EmailMessage
from django.utils.translation import ugettext as _
from django.conf import settings

class ContactFormView(FormView):
    template_name = 'contact/form.html'
    success_url = reverse_lazy('contactformthankyou')
    form_class = ContactForm

    def form_valid(self, form):
        form.save()
        subject = _("A message was sent by") + " " + form.cleaned_data['name']
        message = form.cleaned_data['text']
        from_email = 'no-reply@wilmademunnik.nl' 
        headers = {'Reply-To': form.cleaned_data['email']}
        to = [settings.CONTACT_EMAIL]
        connection = get_connection()
        EmailMessage(subject, message, from_email, to,
                        connection=connection, headers=headers).send()

        return super(ContactFormView, self).form_valid(form)

class ContactFormThankyouView(TemplateView):
    template_name = 'contact/thankyou.html'
