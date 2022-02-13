from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone1 = models.CharField(max_length=20, unique=True)
    phone2 = models.CharField(max_length=20, unique=True)
    cart_no = models.CharField(max_length=200, unique=True)
    address = models.CharField(max_length=400)


    def __str__(self):
        return self.name  + "-" + self.last_name

class Farmer(models.Model):
    farmer_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, unique=True)
    tazkira = models.CharField(max_length=200, unique=True)
    address = models.CharField(max_length=400)

    def __str__(self):
        return f"{self.farmer_name} - {self.last_name}"