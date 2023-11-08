# Generated by Django 4.2.6 on 2023-11-08 17:02

import ccam.core.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("people", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="created_by",
            field=models.ForeignKey(
                on_delete=models.SET(ccam.core.models.get_sentinel_user),
                related_name="%(app_label)s_%(class)s_created_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="sex",
            field=models.CharField(choices=[("M", "Homem"), ("F", "Mulher")], max_length=1),
        ),
        migrations.AlterField(
            model_name="person",
            name="updated_by",
            field=models.ForeignKey(
                on_delete=models.SET(ccam.core.models.get_sentinel_user),
                related_name="%(app_label)s_%(class)s_updated_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
