# Generated by Django 3.1.5 on 2021-03-13 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0001_initial'),
        ('orders', '0002_auto_20210227_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderline',
            name='package',
            field=models.ForeignKey(blank=True, help_text='Seller can package and send packaged order lines together for shipment.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_lines', to='shipping.package'),
        ),
        migrations.DeleteModel(
            name='Package',
        ),
    ]