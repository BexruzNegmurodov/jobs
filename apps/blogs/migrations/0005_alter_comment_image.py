# Generated by Django 4.2.3 on 2023-07-12 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_comment_parent_comment_comment_reply_to_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/comment/'),
        ),
    ]