# Generated by Django 4.2.9 on 2024-01-28 14:08

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_userprofile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(default=django.contrib.auth.models.User, max_length=20),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(default='placeholder.png', upload_to='images'),
        ),
    ]
