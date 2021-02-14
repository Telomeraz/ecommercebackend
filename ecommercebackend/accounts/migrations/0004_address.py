# Generated by Django 3.1.5 on 2021-02-14 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Address Name')),
                ('full_address', models.TextField(verbose_name='Address')),
                ('contact_full_name', models.CharField(max_length=255, verbose_name='Contact Full Name')),
                ('contact_phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Contact Phone Number')),
                ('district', models.CharField(max_length=255, verbose_name='District')),
                ('zip_code', models.CharField(max_length=12, verbose_name='Zip Code')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.city')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]