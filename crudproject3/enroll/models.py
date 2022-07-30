from django.db import models

# Create your models here.
class User(models.Model):
    Enter_Your_question=models.IntegerField()
    First_Choice=models.IntegerField()
    Second_Choice=models.IntegerField()
    Third_Choice=models.IntegerField()
    Fourth_Choice=models.IntegerField()
    Correct_Choice=models.IntegerField()

