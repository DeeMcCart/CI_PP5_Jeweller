# Generated by Django 4.2.9 on 2024-02-14 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_cat6_default_lead_time_stocktype_default_lead_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='lead_time',
        ),
        migrations.AlterField(
            model_name='cat6',
            name='default_lead_time',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
