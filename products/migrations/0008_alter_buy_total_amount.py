# Generated by Django 4.0.2 on 2022-02-07 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_buy_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='total_amount',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=10),
        ),
    ]