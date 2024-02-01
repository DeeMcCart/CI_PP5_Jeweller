# Generated by Django 4.2.9 on 2024-02-01 12:17

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.CharField(default='BILL', max_length=4)),
                ('address_id', models.CharField(editable=False, max_length=4)),
                ('address_label', models.CharField(blank=True, max_length=25, null=True)),
                ('address1', models.CharField(blank=True, max_length=80, null=True)),
                ('address2', models.CharField(blank=True, max_length=80, null=True)),
                ('town_or_city', models.CharField(blank=True, max_length=40, null=True)),
                ('county', models.CharField(blank=True, max_length=80, null=True)),
                ('postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_address', to='checkout.order')),
            ],
            options={
                'ordering': ['order', 'address_id', 'created_on'],
            },
        ),
    ]
