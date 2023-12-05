# Generated by Django 4.2.6 on 2023-12-05 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("seac", "0005_alter_seacstaff_options"),
        ("academics", "0023_subjectdispensal_previous_university_grades_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subjectdispensal",
            name="assessed_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subject_dispensal_assessor",
                to="seac.seacstaff",
            ),
        ),
    ]
