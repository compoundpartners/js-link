from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.template import TemplateDoesNotExist
from django.template.loader import select_template
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from . import models, forms
from .models import JSLinkList, JSLink

LINK_ENABLE_FILE = getattr(
    settings,
    'LINK_ENABLE_FILE',
    False,
)

class LayoutMixin():

    def get_layout(self, context, instance, placeholder):
        return instance.layout

    def get_render_template(self, context, instance, placeholder):
        layout = self.get_layout(context, instance, placeholder)
        if layout:
            template = self.TEMPLATE_NAME % layout
            try:
                select_template([template])
                return template
            except TemplateDoesNotExist:
                pass
        return self.render_template

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context


@plugin_pool.register_plugin
class JSLinkListPlugin(LayoutMixin, CMSPluginBase):
    model = JSLinkList
    TEMPLATE_NAME = 'js-link/link_list__%s.html'
    name = _('Link List')
    render_template = 'js-link/link_list.html'
    admin_preview = False
    allow_children = True
    child_classes = ['JSLinkPlugin',]
    form = forms.JSLinkListForm

    fields = [
        'title',
        'layout',
        'attributes',
    ]


@plugin_pool.register_plugin
class JSLinkPlugin(LayoutMixin, CMSPluginBase):
    model = JSLink
    name = _('Link')
    render_template = 'js-link/link.html'
    TEMPLATE_NAME = 'js-link/link__%s.html'
    parent_classes = ['JSLinkListPlugin',]
    admin_preview = False
    allow_children = False
    form = forms.JSLinkForm

    fields = [
        'layout',
        'icon',
        ('image', 'svg'),
        'text',
        'url',
    ]
    if LINK_ENABLE_FILE:
        fields += [
            'file',
        ]
    fields += [
        'attributes',
    ]

    def get_layout(self, context, instance, placeholder):
        if instance.layout:
            return instance.layout
        instance, _ = instance.parent.get_plugin_instance()
        return instance.layout
