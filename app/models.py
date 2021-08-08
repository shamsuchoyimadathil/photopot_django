from django.db import models

# Create your models here.

class Upload(models.Model):
    description = models.CharField( max_length=50)

class Login(models.Model):
    username = models.CharField( max_length=50)