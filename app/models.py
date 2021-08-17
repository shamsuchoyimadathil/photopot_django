from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin , BaseUserManager

# Create your models here.


class SignUpManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self,username,password,**extra_fields):
        user = self.model(
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user 


    def create_superuser(self,username,password,**extra_fields):
        user = self.create_user(username,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)   

class SignUp(AbstractBaseUser , PermissionsMixin):
    username = models.CharField(max_length=50,unique=True)
    DOB = models.DateField(null=True)
    password = models.CharField(max_length=20)
    confirm_password = models.CharField( max_length=20)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    objects = SignUpManager()

    USERNAME_FIELD = 'username'
    #REQUIRED_FIELDS = ['username','password']




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
    image = models.ImageField(upload_to="images/")