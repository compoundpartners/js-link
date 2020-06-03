# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.utils.text import slugify
from . import models
from .constants import (
    LINK_LIST_LAYOUTS,
)

LINK_LIST_LAYOUT_CHOICES = LINK_LIST_LAYOUTS
if len(LINK_LIST_LAYOUT_CHOICES) == 0 or len(LINK_LIST_LAYOUT_CHOICES[0]) != 2:
    LINK_LIST_LAYOUT_CHOICES = zip(list(map(lambda s: slugify(s).replace('-', '_'), ('',) + LINK_LIST_LAYOUTS)), ('default',) + LINK_LIST_LAYOUTS)

class JSLinkListForm(forms.ModelForm):

    layout = forms.ChoiceField(choices=LINK_LIST_LAYOUT_CHOICES, required=False)

    def __init__(self, *args, **kwargs):
        super(JSLinkListForm, self).__init__(*args, **kwargs)
        if len(LINK_LIST_LAYOUTS) == 0:
            self.fields['layout'].widget = forms.HiddenInput()

    class Meta:
        model = models.JSLinkList
        fields = ['title', 'layout', 'attributes',]
