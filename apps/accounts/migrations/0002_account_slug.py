# Generated by Django 4.2.3 on 2023-07-23 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='slug',
            field=models.SlugField(max_length=221, null=True, unique=True),
        ),
    ]
