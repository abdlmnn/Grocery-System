from django.db import models
import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Unit(models.Model):
    name = models.CharField(max_length=20, unique=True)
    abbreviation = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return f"{self.name} ({self.abbreviation})"

class Inventory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField(default=0)
    unit_type = models.ForeignKey(Unit, on_delete=models.PROTECT, null=True, blank=True,)
    STATUS_CHOICES = [('active', 'Active'),('inactive', 'Inactive'),]
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='active')
    stock_status = models.CharField(max_length=255, default='Stock in')
    date_added = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateField(blank=True, null=True)