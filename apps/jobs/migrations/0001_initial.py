# Generated by Django 4.2.3 on 2023-07-14 11:38

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(null=True, upload_to='job/category')),
                ('name', models.CharField(max_length=221)),
                ('body', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=221)),
                ('image', models.ImageField(upload_to='company/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(max_length=221)),
                ('speciality', models.CharField(max_length=221)),
                ('image', models.ImageField(upload_to='jobs/')),
                ('description', ckeditor.fields.RichTextField()),
                ('gender', models.IntegerField(choices=[(1, 'men'), (2, 'women'), (3, 'no difference')])),
                ('responsibility', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('qualifications', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('Benefits', models.TextField(blank=True, null=True)),
                ('vacancy', models.IntegerField(default=1)),
                ('time', models.IntegerField(choices=[(1, 'full_time'), (2, 'part_time'), (3, 'three days a week'), (4, 'night time'), (5, 'remote(time is not limited)')])),
                ('experience', models.IntegerField(default=0)),
                ('salary', models.IntegerField(default=0)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobs.category')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobs.company')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=221)),
                ('image', models.ImageField(blank=True, null=True, upload_to='jobs/apply')),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.job')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
