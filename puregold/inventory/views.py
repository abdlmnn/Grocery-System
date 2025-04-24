from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q

@login_required()
def product(request):
    if request.method == 'GET':
        search_query = request.GET.get('search', '')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        inventory = Inventory.objects.all()
        if search_query:
            inventory = inventory.filter(Q(name__icontains=search_query) | Q(subcategory__name__icontains=search_query) | Q(brand__name__icontains=search_query))
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
def stock(request):
    if request.method == 'GET':
        search_query = request.GET.get('search', '')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        stock = Stock.objects.all()
        if search_query:
            stock = stock.filter(Q(inventory__name__icontains=search_query) | Q(unit__name__icontains=search_query))
        if start_date:
            stock = stock.filter(created_date__gte=start_date)
        if end_date:
            stock = stock.filter(created_date__lte=end_date)
        paginator = Paginator(stock, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    context = {
        'button': 'Inventory',
        'title': 'Stocks',
        'page_obj': page_obj,
        'stock': page_obj.object_list,
    }
    return render(request, 'stocks.html', context)

@login_required()
def category(request):
    if request.method == 'GET':
        search_query = request.GET.get('search', '')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        category = Category.objects.all()
        if search_query:
            category = category.filter(name__icontains=search_query)
        if start_date:
            category = category.filter(created_date__gte=start_date)
        if end_date:
            category = category.filter(created_date__lte=end_date)
        paginator = Paginator(category, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    context = {
        'button': 'Inventory',
        'title': 'Categories',
        'page_obj': page_obj,
        'category': page_obj.object_list,
    }
    return render(request, 'category.html', context)

@login_required()
def subcategory(request):
    if request.method == 'GET':
        search_query = request.GET.get('search', '')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        subcategory = Subcategory.objects.all()
        if search_query:
            subcategory = subcategory.filter(Q(category__name__contains=search_query) | Q(name__contains=search_query) )
        if start_date:
            subcategory = subcategory.filter(created_date__gte=start_date)
        if end_date:
            subcategory = subcategory.filter(created_date__lte=end_date)
        paginator = Paginator(subcategory, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    context = {
        'button': 'Inventory',
        'title': 'Subcategories',
        'page_obj': page_obj,
        'subcategory': page_obj.object_list,
    }
    return render(request, 'subcategory.html', context)

@login_required()
def brand(request):
    if request.method == 'GET':
        search_query = request.GET.get('search', '')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        brand = Brand.objects.all()
        if search_query:
            brand = brand.filter(name__icontains=search_query)
        if start_date:
            brand = brand.filter(created_date__gte=start_date)
        if end_date:
            brand = brand.filter(created_date__lte=end_date)
        paginator = Paginator(brand, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    context = {
        'button': 'Inventory',
        'title': 'Brands',
        'page_obj': page_obj,
        'brand': page_obj.object_list,
    }
    return render(request, 'brands.html', context)

@login_required()
def unit(request):
    if request.method == 'GET':
        search_query = request.GET.get('search', '')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        unit = Unit.objects.all()
        if search_query:
            unit = unit.filter(name__icontains=search_query)
        if start_date:
            unit = unit.filter(created_date__gte=start_date)
        if end_date:
            unit = unit.filter(created_date__lte=end_date)
        paginator = Paginator(unit, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    context = {
        'button': 'Inventory',
        'title': 'Units',
        'page_obj': page_obj,
        'unit': page_obj.object_list,
    }
    return render(request, 'units.html', context)