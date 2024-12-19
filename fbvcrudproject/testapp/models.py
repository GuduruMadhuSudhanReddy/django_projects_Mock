from django.db import models

# Create your models here.
class Employee(models.Model):
    eno = models.IntegerField()          # Employee number, stored as an integer
    ename = models.CharField(max_length=64)  # Employee name, max length of 64 characters
    esal = models.FloatField()           # Employee salary, stored as a floating-point number
    eaddr = models.CharField(max_length=256) # Employee address, max length of 256 characters
