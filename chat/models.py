from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.http import HttpRequest

# Create your models he
class custom(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    profile_pic=models.ImageField(default='default.jpg',upload_to='images',null=True,blank=True)
    def __str__(self):
        return str(self.user)


    





