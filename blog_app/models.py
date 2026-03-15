from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to='profile_pics/')