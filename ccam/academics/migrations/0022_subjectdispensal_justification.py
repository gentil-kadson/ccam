# Generated by Django 4.2.6 on 2023-12-04 20:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("academics", "0021_knowledgecertificate_justification"),
    ]

    operations = [
        migrations.AddField(
            model_name="subjectdispensal",
            name="justification",
            field=models.TextField(blank=True),
        ),
    ]
