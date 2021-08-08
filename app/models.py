from django.db import models

# Create your models here.


class Upload(models.Model):
    IMAGE_TAGS_CHOICES = (
        ("wallpapers","wallpapers"),
        ("places","places"),
        ("animals","animals"),
        ("beauty","beauty"),
        ("village","village"),
        ("tech","tech"),
    )
    description = models.CharField( max_length=50)
    tag = models.CharField(
        max_length=50,
        choices=IMAGE_TAGS_CHOICES,
    )
    image = models.ImageField()

class SignUp(models.Model):
    username = models.CharField(max_length=50)
    DOB = models.DateField()
    password = models.CharField(max_length=20)
    confirm_password = models.CharField( max_length=20)
    