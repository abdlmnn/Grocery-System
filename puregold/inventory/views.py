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
        inventory = get_filtered_objects(Inventory, search_query, start_date, end_date)
        paginator = Paginator(inventory, 10)
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
        brandID = request.POST['brand']
        if brandID:
            brand = Brand.objects.get(id=brandID)
        else:
            brand = None
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
        'brand': product.brand.name if product.brand else None,
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
        else:
            brand = None
        product.subcategory = subcategory
        product.brand = brand
        product.name = name
        product.description = description
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        product.save()
        return JsonResponse({
            'status': 'success', 
            'message': 'Stock updated.'
        })
    return JsonResponse({
        'status': 'error', 
        'message': 'Invalid request.'
    })

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
            stock = stock.filter(Q(date_added__gte=start_date))
        if end_date:
            stock = stock.filter(Q(date_added__lte=end_date))
        paginator = Paginator(stock, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'button': 'Inventory',
            'title': 'Stocks',
            'page_obj': page_obj,
            'stock': page_obj.object_list,
            'inventory': Inventory.objects.all(),
            'unit': Unit.objects.all(),
        }
    return render(request, 'stocks.html', context)

def addStock(request):
    if request.method == 'POST':
        product = request.POST.get('product')
        quantity = request.POST.get('quantity')
        amountPerUnit = request.POST.get('amountPerUnit') or 0
        unitID = request.POST.get('unit')
        if unitID:
            unit = Unit.objects.get(id=unitID)
        else:
            unit = None
        price = request.POST.get('price')
        expiryDate = request.POST.get('expiryDate') or None
        description = request.POST.get('description')
        inventory = Inventory.objects.get(id=product)
        Stock.objects.create(
            inventory = inventory,
            quantity = quantity,
            amount_per_unit = amountPerUnit,
            unit = unit,
            price = price,
            description = description,
            expiry_date = expiryDate
        ).save()
        return redirect('inventory:stock')
    else:
        return redirect('inventory:stock')

def getImage(request, pID):
    try:
        product = Inventory.objects.get(id=pID)
        if product.image:
            return JsonResponse({
                'status': 'success',
                'message': 'Fetched image.',
                'image': product.image.url
            })
        else:
            return JsonResponse({
                'status': 'error',
                'message': 'No image.'
            })
    except Inventory.DoesNotExist:
        return JsonResponse({
            'status': 'error',
            'message': 'No product id.'
        })

def viewStock(request, pID):
    stock = get_object_or_404(Stock, id=pID)
    data = {
        'status': 'success',
        'message': 'Data is visible.',
        'product': stock.inventory.name,
        'quantity': stock.quantity,
        'amountPerUnit': stock.amount_per_unit or None,
        'unit': stock.unit.name if stock.unit else None,
        'price': stock.price,
        'expiryDate': stock.expiry_date,
        'description': stock.description,
        'image': stock.inventory.image.url,
    }    
    return JsonResponse(data)

def editStock(request, pID):
    stock = get_object_or_404(Stock, id=pID)
    if request.method == 'POST':
        product_id = request.POST.get('product')
        quantity = request.POST.get('quantity')
        amountPerUnit = request.POST.get('amountPerUnit')
        unit_id = request.POST.get('unit')
        price = request.POST.get('price')
        expiryDate = request.POST.get('expiryDate')
        description = request.POST.get('description')
        if product_id:
            product = Inventory.objects.get(id=product_id)
        if unit_id:
            unit = Unit.objects.get(id=unit_id)
        else:
            unit = None
        if amountPerUnit:
            stock.amount_per_unit = amountPerUnit
        else:
            stock.amount_per_unit = None
        
        if expiryDate:
            stock.expiry_date = expiryDate 
        else:
            stock.expiry_date = None
        stock.inventory = product
        stock.quantity = quantity
        stock.unit = unit
        stock.price  = price 
        stock.description = description
        stock.save()
        return JsonResponse({
            'status': 'success', 
            'message': 'Stock updated.'
        })
    return JsonResponse({
        'status': 'error', 
        'message': 'Invalid request.'
    })

def deleteStock(request, pID):
    stock = Stock.objects.get(id=pID)
    stock.delete()
    return redirect('inventory:stock')












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
        paginator = Paginator(category, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    context = {
        'button': 'Inventory',
        'title': 'Categories',
        'page_obj': page_obj,
        'category': page_obj.object_list,
    }
    return render(request, 'category.html', context)

def addCategory(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category = Category.objects.create(
            name = name
        )
        category.save()
        return redirect('inventory:category')
    else:
        return redirect('inventory:category')

def viewCategory(request,cID):
    category = get_object_or_404(Category, id=cID)
    return JsonResponse({
        'status': 'success',
        'message': 'Data visible.',
        'name': category.name,
    })

def editCategory(request,cID):
    category = get_object_or_404(Category, id=cID)
    if request.method == 'POST':
        name = request.POST.get('name')
        category.name = name
        category.save()
        return JsonResponse({
            'status': 'success', 
            'message': 'Category updated.'
        })
    return JsonResponse({
        'status': 'error', 
        'message': 'Invalid request.'
    })

def deleteCategory(request,cID):
    category = Category.objects.get(id=cID)
    category.delete()
    return redirect('inventory:category')










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
        paginator = Paginator(subcategory, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    context = {
        'button': 'Inventory',
        'title': 'Subcategories',
        'page_obj': page_obj,
        'subcategory': page_obj.object_list,
        'category': Category.objects.all()
    }
    return render(request, 'subcategory.html', context)

def addSubCategory(request):
    if request.method == 'POST':
        category = Category.objects.get(id= request.POST.get('category'))
        name = request.POST.get('name')
        subcategory = Subcategory.objects.create(
            category = category,
            name = name,
        )
        subcategory.save()
        return redirect('inventory:subcategory')
    else:
        return redirect('inventory:subcategory')

def viewSubCategory(request,sID):
    subcategory = get_object_or_404(Subcategory, id=sID)
    return JsonResponse({
        'status': 'success',
        'message': 'Data visible.',
        'category': subcategory.category.name,
        'name': subcategory.name,
    })

def editSubCategory(request,sID):
    subcategory = get_object_or_404(Subcategory, id=sID)
    if request.method == 'POST':
        name = request.POST.get('name')
        categoryID = request.POST.get('category')
        if categoryID:
            category = Category.objects.get(id=categoryID)
        subcategory.category = category
        subcategory.name = name
        subcategory.save()
        return JsonResponse({
            'status': 'success', 
            'message': 'Subcategory updated.'
        })
    return JsonResponse({
        'status': 'error', 
        'message': 'Invalid request.'
    })

def deleteSubCategory(request,sID):
    subcategory = Subcategory.objects.get(id=sID)
    subcategory.delete()
    return redirect('inventory:subcategory')










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