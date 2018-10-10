from django.db import models
from cms.models import CMSPlugin
from filer.fields.image import FilerImageField

from django.utils.html import strip_tags
from django.utils.text import Truncator


class JSLinkList(CMSPlugin):

    title = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return Truncator(strip_tags(self.title)).words(3, truncate="...")


class JSLink(CMSPlugin):

    icon = FilerImageField(null=True, blank=True, related_name="icon")
    text = models.CharField(max_length=255, blank=True)
    url = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return Truncator(strip_tags(self.text)).words(3, truncate="...")
