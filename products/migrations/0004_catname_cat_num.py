# Generated by Django 4.2.9 on 2024-01-30 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_catname'),
    ]

    operations = [
        migrations.AddField(
            model_name='catname',
            name='cat_num',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
