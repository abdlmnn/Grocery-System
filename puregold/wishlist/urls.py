from django.urls import path
from .views import *

urlpatterns = [
    # Main
    path('',wishlist, name='wishlist'),
    path('add/<int:stock_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('delete/<int:id>/', delete, name='delete'),
] 
