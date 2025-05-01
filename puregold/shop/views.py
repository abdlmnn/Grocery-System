from django.shortcuts import render
from inventory.models import *

# Create your views here.

def shop(request):
    context = {
        'stocks': Stock.objects.all()
    }
    return render(request,'shop.html', context)

def login(request):
    return render(request,'content/login.html')

def register(request):
    return render(request,'content/register.html')