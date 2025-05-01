from django.db import models
from accounts.models import *
from inventory.models import *

# Create your models here.

class Wishlist(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)