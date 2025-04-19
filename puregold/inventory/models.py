from django.db import models
import datetime
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
        return f'{self.category} - {self.name}'
    
class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'
    
class Unit(models.Model):
    name = models.CharField(max_length=20, unique=True, null=True, blank=True)
    abbreviation = models.CharField(max_length=5, unique=True, null=True, blank=True)
    
def product_image_path(instance, filename):
    return os.path.join('products', str(instance.user.id), filename)

class Inventory(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    product_image = models.ImageField(upload_to=product_image_path, null=True, blank=True)
    product_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField(default=0)
    unit_type = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, blank=True)
    STATUS_CHOICES = [('active', 'Active'),('inactive', 'Inactive'),]
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='active')
    stock_status = models.CharField(max_length=255, default='Stock in')
    date_added = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.subcategory} - {self.brand} - {self.product_name}'