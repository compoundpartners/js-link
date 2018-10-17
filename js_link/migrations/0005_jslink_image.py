# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-17 09:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('js_link', '0004_jslink_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='jslink',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image', to=settings.FILER_IMAGE_MODEL),
        ),
    ]
