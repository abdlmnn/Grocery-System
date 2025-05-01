from django.db import models
from accounts.models import *
from inventory.models import *

# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    STATUS_CHOICES = [
        ('pending', 'Place Orders'),
        ('processing', 'Processing'),
        ('completed', 'Delivered Orders'),
        ('cancelled', 'Canceled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Order #{self.id} - {self.status}"

    def update_total_amount(self):
        total = sum(orderline.total_amount for orderline in self.orderline_set.all())
        self.total_amount = total
        self.save()

class Orderline(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Orderline #{self.id} for {self.stock.inventory.name} - Qty: {self.quantity}"

    def save(self, *args, **kwargs):
        self.total_amount = self.stock.price * self.quantity  
        super().save(*args, **kwargs)
        self.order.update_total_amount() 