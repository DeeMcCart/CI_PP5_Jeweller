# Generated by Django 4.2.9 on 2024-02-25 22:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0023_alter_orderaddress_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='line_ship_date',
            field=models.DateField(default=datetime.date(2024, 3, 1)),
        ),
    ]