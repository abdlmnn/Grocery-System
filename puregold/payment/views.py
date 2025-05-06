from django.shortcuts import render, get_object_or_404, redirect
from .models import Payment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_date
from order.models import *
from inventory.models import *
from django.db.models import Sum, F
from datetime import datetime
from django.db.models import Q

def update_payment_status(request, payment_id):
    if request.method == 'POST':
        payment = get_object_or_404(Payment, pk=payment_id)
        new_status = request.POST.get('status')
        if new_status in ['pending', 'completed']:
            payment.status = new_status
            payment.save()
    return redirect('payment:payment')

def inventory_report(request):
    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')
    stocks = Stock.objects.select_related('inventory', 'unit', 'inventory__brand')
    if search_query:
        stocks = stocks.filter(inventory__name__icontains=search_query)
    if start_date and end_date:
        stocks = stocks.filter(expiry_date__range=[start_date, end_date])
    context = {
        'button': 'Reports',
        'title': 'Inventory Report',
        'stocks': stocks,
        'search_query': search_query,
        'start_date': start_date,
        'end_date': end_date,
    }
    return render(request, 'inventory-report.html', context)

def sales_report(request):
    search_query = request.GET.get('search', '')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    orders = Order.objects.all().prefetch_related('payments', 'customer__user')

    if search_query:
        orders = orders.filter(
            Q(customer__user__first_name__icontains=search_query) |
            Q(customer__user__last_name__icontains=search_query)
        )

    if start_date and end_date:
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')
        orders = orders.filter(date__date__range=[start, end])

    total_sales = orders.aggregate(Sum('total_amount'))['total_amount__sum'] or 0

    context = {
        'button': 'Reports',
        'title': 'Sales Report',
        'orders': orders.order_by('-date'),
        'search_query': search_query,
        'total_sales': total_sales,
        'start_date': start_date or '',
        'end_date': end_date or '',
    }
    return render(request, 'sales-report.html', context)
    

@login_required(login_url='/login/')
def payment(request):
    orders = Order.objects.prefetch_related('payments').all().order_by('-id')
    context = {
        'orders': orders,
        'title': 'Payments',
    }
    return render(request, 'payment.html', context)

@login_required(login_url='/login/')
def gcash_payment_view(request, id):
    payment = get_object_or_404(Payment, id=id)

    if request.method == 'POST':
        uploaded_image = request.FILES.get('image')
        if uploaded_image:
            payment.image = uploaded_image
            payment.status = 'completed' 
            payment.save()
            messages.success(request, "Your GCash proof has been submitted.")
            return redirect('order:thank-you')

    context = {
        'payment': payment
    }
    return render(request, 'gcash.html', context)
