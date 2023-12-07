from django.db import models

class Register(models.Model):
    uname = models.CharField(max_length=30)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=20)
