from django.db import models


# Create your models here.

class Employee(models.Model):
    employee_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, unique=True)
    tazkira = models.CharField(max_length=50, unique=True)
    hire_date = models.DateField()
    salary = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='employee/images', default='user.jpg')
    address = models.CharField(max_length=500)
    

    def __str__(self):
        return f"{self.employee_name} - {self.last_name}"



class Attendance(models.Model):
    STATUS = (
        ("full time", 'full time'),
        ("half time", 'half time'),
        ("absent", 'absent'),
        ("overtime", 'overtime'),
    )
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS, default="full time")
    overtime_amount = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    salary_per_hour = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    

    def __str__(self):
        return f"{self.employee.employee_name}"