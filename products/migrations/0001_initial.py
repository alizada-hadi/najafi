# Generated by Django 4.0.2 on 2022-02-05 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name_en', models.CharField(max_length=200)),
                ('product_name_fa', models.CharField(max_length=200)),
                ('quality', models.CharField(choices=[('sort1', 'sort1'), ('sort2', 'sort2'), ('sort3', 'sort3')], default='sort1', max_length=20)),
                ('quality1', models.CharField(blank=True, choices=[('sortA', 'sortA'), ('sortB', 'sortB')], max_length=20, null=True)),
                ('quantity', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('unite', models.CharField(choices=[('KG', 'KG'), ('SER', 'SER'), ('MANN', 'MANN'), ('CARTOON', 'CARTOON')], default='KG', max_length=20)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_sale', models.CharField(choices=[('export', 'export'), ('local', 'local')], default='local', max_length=20)),
                ('quantity', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('unit', models.CharField(choices=[('KG', 'KG'), ('SER', 'SER'), ('MANN', 'MANN'), ('CARTOON', 'CARTOON')], default='KG', max_length=20)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('recieved_amount', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('remained_amount', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('date_of_sale', models.DateField(blank=True, null=True)),
                ('date_of_send', models.DateTimeField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('unite', models.CharField(choices=[('KG', 'KG'), ('SER', 'SER'), ('MANN', 'MANN'), ('CARTOON', 'CARTOON')], default='KG', max_length=20)),
                ('address', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('total_amount', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('paid_amount', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('remined_amount', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('description', models.TextField(blank=True)),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.employee')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.customer')),
            ],
        ),
    ]
