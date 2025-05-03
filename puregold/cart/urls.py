from django.urls import path
from .views import *

urlpatterns = [
    path('',cart, name='cart'),
    path('add/<int:stock_id>/',add_to_cart, name='add_to_cart'),
    path('delete/<int:id>/', delete, name='delete'),
] 
