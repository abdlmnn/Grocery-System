from django.urls import path, include
from .views import *

urlpatterns = [
    # Main
    path('', payment, name='payment'),
    path('sales-report/', sales_report, name='sales-report'),
    path('inventory-report/', inventory_report, name='inventory-report'),
    path('update-status/<int:payment_id>/', update_payment_status, name='update-status'),
    path('gcash/<int:id>/', gcash_payment_view, name='gcash')
] 
