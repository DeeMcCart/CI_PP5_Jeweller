# Generated by Django 4.2.9 on 2024-02-14 20:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0010_order_order_status_alter_order_delivery_method_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_track',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='planned_ship_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 28, 20, 44, 24, 243995, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='line_ship_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 15, 20, 44, 24, 244761, tzinfo=datetime.timezone.utc)),
        ),
    ]