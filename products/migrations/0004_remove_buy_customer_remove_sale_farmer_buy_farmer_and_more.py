# Generated by Django 4.0.2 on 2022-02-07 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_farmer_alter_customer_address'),
        ('products', '0003_remove_sale_customer_sale_farmer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buy',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='farmer',
        ),
        migrations.AddField(
            model_name='buy',
            name='farmer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.farmer'),
        ),
        migrations.AddField(
            model_name='sale',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='customers.customer'),
            preserve_default=False,
        ),
    ]