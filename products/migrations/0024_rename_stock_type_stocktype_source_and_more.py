# Generated by Django 4.2.9 on 2024-02-18 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_product_source'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stocktype',
            old_name='stock_type',
            new_name='source',
        ),
        migrations.AddField(
            model_name='product',
            name='can_be_engraved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='max_char_engrave',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='item_lead_time',
            field=models.IntegerField(default=1),
        ),
    ]
