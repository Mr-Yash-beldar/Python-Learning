from django.db import models

# Create your models here.
class SignUp(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=25)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
    date = models.DateField()
