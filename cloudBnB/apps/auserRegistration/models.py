from django.db import models

# Create your models here.
class user(models.Model):
    email = models.EmailField(unique=True)
    cellNumber = models.IntegerField(max_length=15)
    profilePic = models.ImageField()