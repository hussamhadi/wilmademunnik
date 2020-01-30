from django.contrib import admin
from models import *

class ImageInline(admin.StackedInline):
    model = Image

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_finished', 'active' )
    inlines = [ImageInline,]
admin.site.register(Project, ProjectAdmin)

class ProjectImageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Image, ProjectImageAdmin)
