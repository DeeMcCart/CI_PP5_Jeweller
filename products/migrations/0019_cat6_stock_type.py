# Generated by Django 4.2.9 on 2024-02-14 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_rename_stock_type_product_cat6_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat6',
            name='stock_type',
            field=models.CharField(blank=True, default='STOCK', max_length=30, null=True),
        ),
    ]
