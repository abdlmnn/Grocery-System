from django.shortcuts import render, redirect
from .models import *
from datetime import datetime

def product(request):
    context = {
        'button': 'Inventory',
        'title': 'Products',
        'timestamp': datetime.now().timestamp(),
    }
    return render(request, 'products.html', context)

def category(request):
    context = {
        'button': 'Inventory',
        'title': 'Categories',
        'timestamp': datetime.now().timestamp(),
    }
    return render(request, 'category.html', context)