from django.urls import path
from .views import *

urlpatterns = [
    
    path('', notifications, name='notifications'),
    path('read-all/', read_all, name='read-all'),
    path('clear-all/', clear_all, name='clear-all'),
    path('read/<int:id>/', read, name='read'),
    path('delete/<int:id>/', delete, name='delete'),
] 
