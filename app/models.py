from django.db import models

# Create your models here.

class Upload(models.Model):
    IMAGE_TAGS_CHOICES = (
        ("wallpapers","wallpapers"),
        ("places","places"),
        ("beauty","beauty"),
        ("village","village"),
        ("Technology","Technology"),
        ("Abstract","Abstract"),
        ("Animals","Animals"),
        ("Drinks","Drinks,"),
        ("Entertainment","Entertainment"),
        ("Food","Food"),
        ("Holidays","Holidays"),
        ("People","People"),
        ("Sports","Sports"),
        ("Vehicles","Vehicles"),
        ("World","World"),
        ("Other","Other"),
    )
    title = models.CharField( max_length=50)
    tag = models.CharField(
        max_length=50,
        choices=IMAGE_TAGS_CHOICES,
    )
    image = models.ImageField(upload_to="images/")