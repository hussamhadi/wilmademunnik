from django.db import models
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3


class Contact(models.Model):
    name = models.CharField(_('Name'), max_length=300)
    email = models.EmailField()
    text = models.TextField(_('Message'))
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    def send_email(self):
        return '<a href=mailto:%s?subject=%s&body=%s>Send Email</a>' % (self.email, 'RE: Een email is verstuurd door ' + self.name, self.text)
    send_email.allow_tags = True

    class Meta:
        ordering = ['-created']
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')


class ContactForm(ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV3)
    class Meta:
        model = Contact
        exclude = []
