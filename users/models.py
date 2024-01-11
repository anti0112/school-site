from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    
class Student(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
    

    
    
