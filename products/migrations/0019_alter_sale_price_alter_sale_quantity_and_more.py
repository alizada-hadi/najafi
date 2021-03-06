# Generated by Django 4.0.2 on 2022-02-13 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_alter_sale_price_alter_sale_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='price',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='sale',
            name='quantity',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='sale',
            name='recieved_amount',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='sale',
            name='remained_amount',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='sale',
            name='total_price',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=8),
        ),
    ]
