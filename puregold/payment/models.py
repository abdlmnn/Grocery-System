from django.db import models
from accounts.models import *
from order.models import *

# Create your models here.

def payments_image_path(instance, filename):
    return os.path.join('payments', str(instance.customer.user.id), filename)

class Payment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    
    PAYMENT_METHOD_CHOICES = [
        ('cod', 'Cash on Delivery'),
        ('gcash', 'GCash'),
        ('paypal', 'PayPal'),
    ]
    method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES, default='cod')
    image = models.ImageField(upload_to=payments_image_path, null=True, blank=True)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    date = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Payment for Order #{self.order.id} by {self.customer.user.first_name} {self.customer.user.last_name} - {self.get_status_display()}"