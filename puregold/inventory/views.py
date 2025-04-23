from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.paginator import Paginator

@login_required()
def product(request):
    if request.method == 'GET':
        search_query = request.GET.get('search', '')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        inventory = Inventory.objects.all()
        if search_query:
            inventory = inventory.filter(name__icontains=search_query)
        if start_date:
            inventory = inventory.filter(created_date__gte=start_date)
        if end_date:
            inventory = inventory.filter(created_date__lte=end_date)
        paginator = Paginator(inventory, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    context = {
        'button': 'Inventory',
        'title': 'Products',
        'page_obj': page_obj,
        'inventory': page_obj.object_list,
    }
    return render(request, 'products.html', context)

@login_required()
def category(request):
    context = {
        'button': 'Inventory',
        'title': 'Categories',
    }
    return render(request, 'category.html', context)

@login_required()
def brand(request):
    context = {
        'button': 'Inventory',
        'title': 'Brands',
    }
    return render(request, 'brands.html', context)