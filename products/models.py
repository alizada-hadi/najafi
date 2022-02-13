from email.mime import image
from django.db import models
from customers.models import Customer, Farmer
from employees.models import Employee

# Create your models here.
"""
1- employee
2- customer
3- buy
4- product
5- sell
"""

class Buy(models.Model):
    UNITE = (
        ('KG','KG'),
        ('SER', 'SER'),
        ('MANN','MANN'),
        ('CARTOON', 'CARTOON'),
    )
    name = models.CharField(max_length=200)
    farmer = models.ForeignKey(Farmer, on_delete=models.SET_NULL, null=True)
    buyer = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    quantity = models.DecimalField(decimal_places=4, max_digits=8, default=0)
    unite = models.CharField(max_length=20, choices=UNITE, default="KG")
    address = models.CharField(max_length=500)
    date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    paid_amount = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    remined_amount = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    description = models.CharField(max_length=500, blank=True , null=True)


    def save(self, *args, **kwargs):
        if not self.total_amount:
            self.total_amount = self.quantity * self.price
        if not self.remined_amount:
            self.remined_amount = self.total_amount - self.paid_amount
        
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name





class Product(models.Model):
    QUALITIES =(
        ('sort1','sort1'),
        ('sort2', 'sort2'),
        ('sort3','sort3'),
    )
    QUALITIES1 = (
        ('sortA', 'sortA'),
        ('sortB', 'sortB'),
    )
    UNITE = (
        ('KG','KG'),
        ('SER', 'SER'),
        ('MANN','MANN'),
        ('CARTOON', 'CARTOON'),
    )
    # lot_number = models.PositiveIntegerField(primary_key=True, unique=True)
    product_name_en = models.CharField(max_length=200, verbose_name="Product Name / English")
    product_name_fa = models.CharField(max_length=200, verbose_name="Product Name / Dari")
    quality = models.CharField(max_length=20, choices=QUALITIES, default= 'sort1')
    quality1 = models.CharField(max_length=20, choices=QUALITIES1, null=True, blank=True)
    quantity = models.DecimalField(default=0, decimal_places=4, max_digits=10)
    unite = models.CharField(max_length=20, choices=UNITE, default="KG")
    price = models.DecimalField(decimal_places=4, max_digits=10, default=0)
    total_price = models.DecimalField(decimal_places=4,max_digits=10,default=0)
    photo = models.ImageField(upload_to='product/images', default='product.jpg')
    store_date = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
         if not self.total_price:
            self.total_price = self.quantity * self.price
         super().save(*args, **kwargs)
         
    def __str__(self):
        return self.product_name_en


class Sale(models.Model):
    SALE_TYPE = (
        ("export", "export"),
        ("local", "local"),
    )
    UNITE = (
        ('KG','KG'),
        ('SER', 'SER'),
        ('MANN','MANN'),
        ('CARTOON', 'CARTOON'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    type_of_sale = models.CharField(max_length=20, choices=SALE_TYPE, default="local")
    quantity = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    unit = models.CharField(max_length=20, choices=UNITE, default="KG")
    price = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    # 
    total_price = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    recieved_amount = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    remained_amount = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    date_of_sale = models.DateField(null=True, blank=True)
    date_of_send = models.DateTimeField(null=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.total_price:
            self.total_price = self.quantity * self.price
        if not self.recieved_amount:
            self.recieved_amount = self.total_price - self.recieved_amount
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.product_name_en} - {self.product.quality} - {self.product.quality1}"




