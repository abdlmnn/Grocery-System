from django.db import models
import datetime
from django.utils import timezone
import os

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'
    
class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'
    
class Unit(models.Model):
    name = models.CharField(max_length=20, unique=True, null=True, blank=True)
    abbreviation = models.CharField(max_length=5, unique=True, null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'
    
def product_image_path(instance, filename):
    return os.path.join('products', filename)

class Inventory(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to=product_image_path, default='products/default-noimage.jpg', null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

class Stock(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    amount_per_unit = models.DecimalField(default=0, max_digits=6, decimal_places=2, null=True, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE,  blank=True, null=True)
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateField(blank=True, null=True)
    is_empty = models.BooleanField(default=False)
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('out_of_stock', 'Out of Stock'),
        ('expired', 'Expired'),
    ]
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return f'{self.inventory.name} - {self.quantity} {self.unit} @ ₱{self.price}'