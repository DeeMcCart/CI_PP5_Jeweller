# Generated by Django 4.2.9 on 2024-02-14 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_rename_cat6_value_product_stock_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_type', models.CharField(blank=True, max_length=30, null=True)),
            ],
        
        ),
    ]
