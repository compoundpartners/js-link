# -*- coding: utf-8 -*-

from django.conf import settings

LINK_LIST_LAYOUTS = getattr(
    settings,
    'LINK_LIST_LAYOUTS',
    (),
)

LINK_LAYOUTS = getattr(
    settings,
    'LINK_LAYOUTS',
    (),
)
