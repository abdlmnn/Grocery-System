from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.core.paginator import Paginator
from accounts.models import Customer


@login_required
def admin(request):
    if not request.user.is_superuser:
        return redirect('shop:shop')
    search_query = request.GET.get('search', '')
    if search_query:
        admins = User.objects.filter(is_superuser=True, email__icontains=search_query)
    else:
        admins = User.objects.filter(is_superuser=True)
    context = {
        'button': 'Administration',
        'title': 'Admin',
        'admins': admins,
        'search_query': search_query,
    }
    return render(request, 'admin.html', context)


@login_required
def customers(request):
    if not request.user.is_superuser:
        return redirect('shop:shop')
    search_query = request.GET.get('search', '')
    customers = Customer.objects.select_related('user').all()
    if search_query:
        customers = customers.filter(
            user__first_name__icontains=search_query
        ) | customers.filter(
            user__last_name__icontains=search_query
        ) | customers.filter(
            user__email__icontains=search_query
        )
    context = {
        'button': 'Administration',
        'title': 'Customers',
        'customers': customers,
        'search_query': search_query,
    }
    return render(request, 'customers.html', context)


def delete(request, id):
    if not request.user.is_superuser:
        return redirect('shop:shop')
    customer = Customer.objects.get(id=id)
    if customer:
        customer.user.delete()
        return redirect('accounts:customers')
    admin = get_object_or_404(User, id=id, is_superuser=True)
    if admin == request.user:
        return redirect('accounts:admin')
    if admin: 
        admin.delete()
        return redirect('accounts:admin')
def delete(request, id):
    if not request.user.is_superuser:
        return redirect('shop:shop')

    try:
        customer = Customer.objects.get(id=id)
        customer.user.delete()
        return redirect('accounts:customers')
    except Customer.DoesNotExist:
        try:
            admin = get_object_or_404(User, id=id, is_superuser=True)
            if admin == request.user:
                messages.warning(request, "You cannot delete yourself.")
                return redirect('accounts:admin')
            admin.delete()
            messages.success(request, "Admin deleted successfully.")
            return redirect('accounts:admin')
        except User.DoesNotExist:
            messages.error(request, "User not found.")
            return redirect('accounts:admin')
    