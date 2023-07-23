# Generated by Django 4.2.3 on 2023-07-22 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0007_apply_is_being_considered_apply_to_accept_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='Cover_letter',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='apply',
            name='candidate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='apply',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jobs.job'),
        ),
    ]
