from django.db import models

# Create your models here.
class Student(models.Model):
    Question=models.CharField(default='python',max_length=100)
    Choice1=models.IntegerField()
    Choice2=models.IntegerField()
    Choice3=models.IntegerField()
    Choice4=models.IntegerField()
    Right_Choice=models.IntegerField()