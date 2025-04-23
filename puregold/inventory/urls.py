from django.urls import path
from .views import *

urlpatterns = [
    # Main
    path('',product,name='product'),
    path('categories/',category,name='category'),
    path('brands/',brand,name='brand'),
] 
