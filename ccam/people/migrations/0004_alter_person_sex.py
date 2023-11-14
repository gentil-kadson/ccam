# Generated by Django 4.2.6 on 2023-11-14 12:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("people", "0003_person_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="sex",
            field=models.CharField(choices=[("M", "Masculino"), ("F", "Feminino")], max_length=1, verbose_name="Sexo"),
        ),
    ]
