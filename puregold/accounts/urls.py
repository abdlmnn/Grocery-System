from django.urls import path
from .views import *

urlpatterns = [
    path('admin/',admin, name='admin'),
    path('customers/',customers, name='customers'),
    path('delete/<int:id>',delete, name='delete'),
] 
