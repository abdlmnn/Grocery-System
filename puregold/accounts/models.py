from django.db import models
from django.contrib.auth.models import User, AbstractUser
import datetime
import os

# Create your models here.

def profile_image_path(instance, filename):
    return os.path.join('profiles', str(instance.user.id), filename)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to=profile_image_path, null=True, blank=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"