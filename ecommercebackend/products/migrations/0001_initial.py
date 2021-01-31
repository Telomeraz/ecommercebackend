# Generated by Django 3.1.5 on 2021-01-31 17:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Product name')),
                ('subheading', models.CharField(blank=True, max_length=255, verbose_name='Product subheading')),
                ('description', models.TextField(blank=True, verbose_name='Product description')),
                ('currency', models.CharField(choices=[('USD', '$'), ('EUR', '€'), ('TRY', '₺')], default='TRY', max_length=3, verbose_name='Currency')),
                ('tax_rate', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Price tax rate')),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created Date and Time')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is product active?')),
                ('is_archived', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(blank=True, max_length=255, null=True, verbose_name='Barcode')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Price')),
                ('purchase_price', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=12, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Purchase price')),
                ('list_price', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=12, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='List price')),
                ('stock', models.PositiveIntegerField(default=0, verbose_name='Stock')),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created Date and Time')),
                ('is_primary', models.BooleanField(default=False, verbose_name='Is variant primary?')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is variant active?')),
                ('is_archived', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='products.product')),
            ],
            options={
                'verbose_name': 'Product variant',
                'verbose_name_plural': 'Product variants',
            },
        ),
    ]
