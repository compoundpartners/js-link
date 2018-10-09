from django.db import models
from cms.models import CMSPlugin
from filer.fields.image import FilerImageField


class JSLinkList(CMSPlugin):

    title = models.CharField(max_length=255, blank=True)


class JSLink(CMSPlugin):

    icon = FilerImageField(null=True, blank=True, related_name="icon")
    text = models.CharField(max_length=255, blank=True)
    url = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.text()
