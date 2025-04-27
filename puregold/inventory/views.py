from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse

def get_filtered_objects(model, search_query=None, start_date=None, end_date=None):
    queryset = model.objects.all()
    if search_query:
        queryset = queryset.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))
    if start_date:
        queryset = queryset.filter(created_date__gte=start_date)
    if end_date:
        queryset = queryset.filter(created_date__lte=end_date)
    return queryset

@login_required()
def product(request):
    if request.method == 'GET':
        search_query = request.GET.get('search', '')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        # inventory = Inventory.objects.all()
        # if search_query:
        #     inventory = inventory.filter(Q(name__icontains=search_query) | Q(subcategory__name__icontains=search_query) | Q(brand__name__icontains=search_query))
        # if start_date:
        #     inventory = inventory.filter(created_date__gte=start_date)
        # if end_date:
        #     inventory = inventory.filter(created_date__lte=end_date)
        inventory = get_filtered_objects(Inventory, search_query, start_date, end_date)
        paginator = Paginator(inventory, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    context = {
        'button': 'Inventory',
        'title': 'Products',
        'page_obj': page_obj,
        'inventory': page_obj.object_list,
        'subcategory': Subcategory.objects.all(),
        'brand': Brand.objects.all(),
    }
    return render(request, 'products.html', context)

def addProduct(request):
    if request.method == 'POST':
        subcat = Subcategory.objects.get(id=request.POST['subcategory'])
        brand = Brand.objects.get(id=request.POST['brand'])
        name = request.POST.get('name')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        inventory = Inventory.objects.create(
            subcategory=subcat,
            brand=brand,
            name=name,
            image=image,
            description=description,
        )
        inventory.save()
        return redirect('inventory:product')
    else:
        return redirect('inventory:product')

def viewProduct(request, pID):
    product = get_object_or_404(Inventory, id=pID)
    data = {
        'status': 'success',
        'message': 'Data is visible.',
        'subcategory': product.subcategory.name if product.subcategory else '',
        'brand': product.brand.name if product.brand else '',
        'name': product.name,
        'image': product.image.url,
        'description': product.description,
    }    
    return JsonResponse(data)
    
def editProduct(request, pID):
    product = get_object_or_404(Inventory, id=pID)
    if request.method == 'POST':
        subcategory_id = request.POST.get('subcategory')
        brand_id = request.POST.get('brand')
        name = request.POST.get('name')
        description = request.POST.get('description')
        if subcategory_id:
            subcategory = Subcategory.objects.get(id=subcategory_id)
        if brand_id:
            brand = Brand.objects.get(id=brand_id)
        product.subcategory = subcategory
        product.brand = brand
        product.name = name
        product.description = description
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        product.save()
        return JsonResponse({'status': 'success', 'message': 'Product updated.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request.'})

def deleteProduct(request, pID):
    product = Inventory.objects.get(id=pID)
    product.delete()
    return redirect('inventory:product')

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