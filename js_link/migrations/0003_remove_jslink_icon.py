# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-10 05:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('js_link', '0002_auto_20181010_0528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jslink',
            name='icon',
        ),
    ]
