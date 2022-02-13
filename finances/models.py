from django.db import models
from employees.models import Employee
from products.models import Sale
# Create your models here.

class Expence(models.Model):
    PERSONAL = (
        ("yes", "yes"),
        ("no", "no"),
    )
    EXPENCE_FOR = (
        ("electricity", "electricity"),
        ("rate", "rate"),
        ("water", "water"),
        ("food", "food"),
        ("stationary", "stationary"),
        ("packaging cost", "packaging cost"),
        ("transport cost", "transport cost"),
        ("maintenance cost", "maintenance cost"),
        ("other", "other"),
    )
    emp_name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    personal_exp = models.CharField(max_length=20, choices=PERSONAL, default="no")
    expence_for = models.CharField(max_length=20, choices=EXPENCE_FOR)
    expence_amount = models.DecimalField(decimal_places=2, max_digits=6, default=0)


class Income(models.Model):
    sale  = models.ForeignKey(Sale, on_delete=models.CASCADE)
    number_of_cash = models.CharField(max_length=100, unique=True)
    amount_of_money = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    sender = models.ForeignKey(Employee, on_delete=models.CASCADE)
    reciever = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="reciever")
    recived_date = models.DateField()

    def __str__(self):
        return f"income from {self.sale} "

