# Generated by Django 4.2.6 on 2023-11-07 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("people", "0001_initial"),
        ("seac", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="seacstaff",
            options={"verbose_name": "SEAC Staff", "verbose_name_plural": "SEAC Staff"},
        ),
        migrations.AddField(
            model_name="seacstaff",
            name="person",
            field=models.OneToOneField(
                default=1, on_delete=django.db.models.deletion.CASCADE, related_name="person", to="people.person"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="seacstaff",
            name="phone_line",
            field=models.CharField(default=232323, max_length=14),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="seacstaff",
            name="role",
            field=models.CharField(choices=[("CO", "Coordenador"), ("FU", "Funcionário")], default="CO", max_length=2),
            preserve_default=False,
        ),
    ]
