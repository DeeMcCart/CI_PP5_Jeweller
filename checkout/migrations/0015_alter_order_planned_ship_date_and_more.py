# Generated by Django 4.2.9 on 2024-02-14 21:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0014_alter_order_planned_ship_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='planned_ship_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 28, 21, 56, 2, 397339, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='line_ship_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 15, 21, 56, 2, 398197, tzinfo=datetime.timezone.utc)),
        ),
    ]
