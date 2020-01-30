from django.conf.urls import url
from contact.views import ContactFormView, ContactFormThankyouView

urlpatterns = [
    url(r'^$', ContactFormView.as_view(), name='contactform'),
    url(r'^thankyou/$', ContactFormThankyouView.as_view(), name='contactformthankyou'),
]
