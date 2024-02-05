# Generated by Django 4.2.9 on 2024-02-01 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_rename_order_line_orderlineitem_line_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=150, max_digits=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]