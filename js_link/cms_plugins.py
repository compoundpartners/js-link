from django.utils.translation import ugettext_lazy as _
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from .models import JSLinkList, JSLink


@plugin_pool.register_plugin
class JSLinkListPlugin(CMSPluginBase):
    model = JSLinkList
    name = _('Link List')
    render_template = 'js-link/link_list.html'
    admin_preview = False
    allow_children = True
    child_classes = ['JSLinkPlugin',]

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context


@plugin_pool.register_plugin
class JSLinkPlugin(CMSPluginBase):
    model = JSLink
    name = _('Link')
    render_template = 'js-link/link.html'
    admin_preview = False
    allow_children = False

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context
