# Generated by Django 4.2.6 on 2023-11-14 20:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("seac", "0004_alter_seacstaff_phone_line_alter_seacstaff_role"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="seacstaff",
            options={"verbose_name": "Funcionário da SEAC", "verbose_name_plural": "Funcionários da SEAC"},
        ),
    ]
