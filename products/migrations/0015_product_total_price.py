# Generated by Django 4.0.2 on 2022-02-13 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_alter_product_product_name_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='total_price',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=10),
        ),
    ]