from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField(max_length=80)
    address=models.CharField(max_length=55)



