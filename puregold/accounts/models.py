from django.db import models
from django.contrib.auth.models import User, AbstractUser
import datetime
import os
import uuid

# Create your models here.
def profile_image_path(instance, filename):
    return os.path.join('profiles', str(instance.user.id), filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to=profile_image_path, default='profile/default.jpg', null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reset_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Password reset for {self.user.username} at {self.created_when}'