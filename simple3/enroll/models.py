from django.db import models

# Create your models here.
class Student(models.Model):
    Email_address=models.EmailField(max_length=100)
    Password=models.CharField(max_length=50)
    Check_me_out=models.CharField(max_length=50)