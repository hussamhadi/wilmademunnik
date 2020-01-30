from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from filebrowser.sites import site

admin.autodiscover()

urlpatterns = [
    url(r'^robots.txt$', TemplateView.as_view(template_name='extra/robots.txt')),
    url(r'^4c391b19ffe0a13c3aef869493027cc5.txt$', TemplateView.as_view(template_name='extra/empty.txt')),
    url(r'^filer/', include('filer.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
]

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns = [
        url(r'^rosetta/', include('rosetta.urls')),
    ] + urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
