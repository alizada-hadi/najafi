# Generated by Django 4.0.2 on 2022-02-13 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_product_store_date_alter_product_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name_en',
            field=models.CharField(max_length=200, verbose_name='Product Name / English'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name_fa',
            field=models.CharField(max_length=200, verbose_name='Product Name / Dari'),
        ),
    ]
