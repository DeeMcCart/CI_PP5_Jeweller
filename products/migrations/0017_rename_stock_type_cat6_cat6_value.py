# Generated by Django 4.2.9 on 2024-02-14 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_cat6_alter_product_stock_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cat6',
            old_name='cat6_value',
            new_name='cat6_value',
        ),
    ]
