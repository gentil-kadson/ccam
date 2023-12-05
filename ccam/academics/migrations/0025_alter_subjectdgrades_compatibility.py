# Generated by Django 4.2.6 on 2023-12-05 12:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("academics", "0024_alter_subjectdispensal_assessed_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subjectdgrades",
            name="compatibility",
            field=models.PositiveSmallIntegerField(
                blank=True, validators=[django.core.validators.MaxValueValidator(100)], verbose_name="Compatibilidade"
            ),
        ),
    ]
