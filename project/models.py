from django.db import models
from django.utils.translation import ugettext as _
from filer.fields.image import FilerImageField


class Project(models.Model):
    active = models.BooleanField(_("Active"), default=True)
    title = models.CharField(_("Title"), max_length=250)
    date_finished = models.DateField(_("Date finished"))
    description = models.TextField(_("Description"))

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return self.pk

    def get_first_image(self):
        image = Image.objects.filter(project=self)
        try:
            return image[0]
        except IndexError:
            return None

    def get_images(self):
        return Image.objects.filter(project=self)

    class Meta:
        ordering = ['-date_finished', ]
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")


class Image(models.Model):
    project = models.ForeignKey(Project, related_name='images')
    image = FilerImageField(null=True, blank=True)
    description = models.CharField(_("Description"), max_length=500)
