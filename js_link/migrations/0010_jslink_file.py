# Generated by Django 2.2.13 on 2020-06-26 10:13

from django.db import migrations
import django.db.models.deletion
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0011_auto_20190418_0137'),
        ('js_link', '0009_auto_20200305_0502'),
    ]

    operations = [
        migrations.AddField(
            model_name='jslink',
            name='file',
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='filer.File', verbose_name='File'),
        ),
    ]
