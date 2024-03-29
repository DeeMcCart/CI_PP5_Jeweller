# Generated by Django 4.2.9 on 2024-03-03 01:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0027_alter_orderlineitem_line_ship_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='planned_ship_date',
            field=models.DateField(default=datetime.date(2024, 3, 8)),
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='line_ship_date',
            field=models.DateField(default=datetime.date(2024, 3, 8)),
        ),
    ]
