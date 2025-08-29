# payroll/models.py
from django.db import models

class Employee(models.Model):
    emp_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.name
