# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-25 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('js_link', '0006_auto_20190621_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='jslinklist',
            name='layout',
            field=models.CharField(blank=True, default='', max_length=60, verbose_name='layout'),
        ),
    ]
