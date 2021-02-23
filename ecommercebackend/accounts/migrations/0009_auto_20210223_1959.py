# Generated by Django 3.1.5 on 2021-02-23 19:59

import django.core.validators
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='contact_full_name',
            field=models.CharField(max_length=255, verbose_name='Contact full name'),
        ),
        migrations.AlterField(
            model_name='address',
            name='contact_phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Contact phone number'),
        ),
        migrations.AlterField(
            model_name='address',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Address name'),
        ),
        migrations.AlterField(
            model_name='address',
            name='zip_code',
            field=models.CharField(max_length=12, verbose_name='Zip code'),
        ),
        migrations.AlterField(
            model_name='country',
            name='alpha2_code',
            field=models.CharField(max_length=2, unique=True, verbose_name='Alpha-2 code'),
        ),
        migrations.AlterField(
            model_name='country',
            name='alpha3_code',
            field=models.CharField(max_length=3, unique=True, verbose_name='Alpha-3 code'),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Country name'),
        ),
        migrations.AlterField(
            model_name='country',
            name='numeric_code',
            field=models.PositiveSmallIntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(999)], verbose_name='Numeric code'),
        ),
    ]