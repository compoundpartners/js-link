from django.db import models
from cms.models import CMSPlugin

from djangocms_icon.fields import Icon

from django.utils.html import strip_tags
from django.utils.text import Truncator


class JSLinkList(CMSPlugin):

    title = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return Truncator(strip_tags(self.title)).words(3, truncate="...")


class JSLink(CMSPlugin):

    icon = Icon(blank=False, default='fa-')
    text = models.CharField(max_length=255, blank=True)
    url = models.CharField(max_length=255)

    def __str__(self):
        if self.text:
            return Truncator(strip_tags(self.text)).words(3, truncate="...")
        elif self.url:
            return strip_tags(self.url)
