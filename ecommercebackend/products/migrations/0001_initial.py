# Generated by Django 3.1.5 on 2021-02-25 20:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='products.attribute')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_archived', models.BooleanField(default=False, help_text='This is a flag that represents whether deleted. True means deleted.')),
                ('name', models.CharField(max_length=255, verbose_name='Product name')),
                ('subheading', models.CharField(blank=True, max_length=255, verbose_name='Product subheading')),
                ('description', models.TextField(blank=True, verbose_name='Product description')),
                ('currency', models.CharField(choices=[('USD', '$'), ('EUR', '€'), ('TRY', '₺')], max_length=3, verbose_name='Currency')),
                ('tax_rate', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Price tax rate')),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created date and time')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is product active?')),
                ('values', models.ManyToManyField(blank=True, related_name='products', to='products.AttributeValue')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='VarianterAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VarianterAttributeValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('varianter_attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='varianter_values', to='products.varianterattribute')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_archived', models.BooleanField(default=False, help_text='This is a flag that represents whether deleted. True means deleted.')),
                ('barcode', models.CharField(blank=True, max_length=255, verbose_name='Barcode')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Price')),
                ('purchase_price', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=12, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Purchase price')),
                ('list_price', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=12, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='List price')),
                ('stock', models.PositiveIntegerField(default=0, verbose_name='Stock')),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created date and time')),
                ('is_primary', models.BooleanField(default=False, verbose_name='Is variant primary?')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is variant active?')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='products.product')),
                ('values', models.ManyToManyField(blank=True, related_name='product_variants', to='products.VarianterAttributeValue')),
            ],
            options={
                'verbose_name': 'Product variant',
                'verbose_name_plural': 'Product variants',
            },
        ),
    ]
