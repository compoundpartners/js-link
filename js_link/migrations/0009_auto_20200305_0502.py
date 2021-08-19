# Generated by Django 2.2.10 on 2020-03-05 05:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('js_link', '0008_jslink_attributes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jslink',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image', to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AlterField(
            model_name='jslink',
            name='url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]