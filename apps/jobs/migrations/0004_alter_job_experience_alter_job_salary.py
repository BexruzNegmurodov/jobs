# Generated by Django 4.2.3 on 2023-07-18 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_remove_job_image_remove_job_speciality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='experience',
            field=models.CharField(max_length=221),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.CharField(max_length=221),
        ),
    ]
