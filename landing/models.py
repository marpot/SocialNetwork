from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Profile(models.Model):
     user = models.CharField(max_length=20)
     id_user = models.CharField(max_length=20)
     bio = models.CharField(max_length=20)
     profileimg = models.ImageField()
     location = models.CharField(max_length=20)

class RegisterUser(models.Model):
     name = models.CharField(max_length=100)
     email = models.EmailField(blank=True)
     password1 = models.CharField(max_length=50)
     password2 = models.CharField(max_length=50)