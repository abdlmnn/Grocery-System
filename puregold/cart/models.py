from django.db import models
from accounts.models import *
from inventory.models import *

# Create your models here.

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('abandoned', 'Abandoned'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return f"{self.customer.user.first_name} {self.customer.user.last_name} - {self.get_status_display()}"

class Cartline(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.stock.inventory.name} - Qty: {self.quantity}"

    def save(self, *args, **kwargs):
        self.total_amount = self.stock.price * self.quantity
        super().save(*args, **kwargs)