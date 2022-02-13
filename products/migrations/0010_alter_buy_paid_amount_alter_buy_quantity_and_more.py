# Generated by Django 4.0.2 on 2022-02-07 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_buy_paid_amount_alter_buy_remined_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='paid_amount',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='buy',
            name='quantity',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='buy',
            name='remined_amount',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=8),
        ),
    ]
