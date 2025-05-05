from django.urls import path, include
from .views import *

urlpatterns = [
    # Main
    path('gcash/<int:id>/', gcash_payment_view, name='gcash')
] 
