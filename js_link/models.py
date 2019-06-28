from django.db import models
from cms.models import CMSPlugin

from djangocms_icon.fields import Icon
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from djangocms_attributes_field.fields import AttributesField

from django.utils.html import strip_tags
from django.utils.text import Truncator

from django.utils.translation import ugettext_lazy as _

class JSLinkList(CMSPlugin):

    title = models.CharField(max_length=255, blank=True)
    layout = models.CharField(
        blank=True,
        default='',
        max_length=60,
        verbose_name=_('layout')
    )
    attributes = AttributesField(verbose_name='Attributes', blank=True)

    def __str__(self):
        return Truncator(strip_tags(self.title)).words(3, truncate="...")


class JSLink(CMSPlugin):

    icon = Icon(blank=False, default='fa-')
    image = FilerImageField(null=True, blank=True, related_name="image")
    text = models.CharField(max_length=255, blank=True)
    url = models.CharField(max_length=255)
    svg = FilerFileField(verbose_name='SVG Image', blank=True, null=True, on_delete=models.SET_NULL, related_name='+')

    def copy_relations(self, oldinstance):
        self.image = oldinstance.image
        self.svg = oldinstance.svg

    def __str__(self):
        if self.text:
            return Truncator(strip_tags(self.text)).words(3, truncate="...")
        elif self.url:
            return strip_tags(self.url)

    @property
    def img_src(self):
        if self.svg:
            return self.svg.url
        elif self.image:
            return self.image.url
        return ''
