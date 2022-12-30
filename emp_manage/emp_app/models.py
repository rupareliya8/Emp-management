from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=100)
    emp_id=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    working=models.BooleanField(default=True)
    department=models.CharField(max_length=10)

    def __str__(self):
        return self.name