# Generated by Django 4.2.6 on 2023-11-14 12:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("seac", "0003_alter_seacstaff_created_by_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="seacstaff",
            name="phone_line",
            field=models.CharField(max_length=14, unique=True, verbose_name="Fone Ramal"),
        ),
        migrations.AlterField(
            model_name="seacstaff",
            name="role",
            field=models.CharField(
                choices=[("CO", "Coordenador"), ("FU", "Funcionário")], max_length=2, verbose_name="Responsabilidade"
            ),
        ),
    ]
