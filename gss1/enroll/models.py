from django.db import models

# Create your models here.
class Student(models.Model):
    studenttpassword=models.CharField(max_length=100,default=" ")
    studenttname=models.CharField(max_length=50)
    studenttemail=models.EmailField(max_length=45)









