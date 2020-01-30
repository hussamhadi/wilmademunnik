from django.contrib import admin
from models import *

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created', 'send_email' )

admin.site.register(Contact, ContactAdmin)
