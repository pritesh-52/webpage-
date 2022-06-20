from django.db import models

# Create your models here.

class user(models.Model):
    Fname=models.CharField(max_length=10)
    Lname=models.CharField(max_length=10)
    Email=models.EmailField()
    Contact=models.CharField(max_length=12)
    Password=models.CharField(max_length=8)

