from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse
from accounts.models import PasswordReset, Customer
from inventory.models import *
from django.db.models import Q
from django.core.serializers.json import DjangoJSONEncoder
import json
from collections import Counter
from django.db.models import Sum
from order.models import Order
from notification.models import *

@login_required
def dashboard(request):
    if not request.user.is_superuser:
        messages.error(request, 'Unauthorized to access the admin.')
        return redirect('shop:shop')
    total_orders = Order.objects.count()
    total_products = Inventory.objects.count()
    total_customers = Customer.objects.count()
    total_sales = Order.objects.aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    labels = []
    data = []
    labels2 = []
    data2 = []
    stock = Stock.objects.select_related('inventory')
    sub = Stock.objects.select_related('inventory')
    for x in stock:
        labels.append(x.inventory.name)
        data.append(x.quantity)
    for x in sub:
        labels2.append(x.inventory.name)
        data2.append(x.quantity)
    
    context = {
        'title': 'Dashboard',
        'total_orders': total_orders,
        'total_products': total_products,
        'total_customers': total_customers,
        'total_sales': total_sales,

        'labels': json.dumps(labels, cls=DjangoJSONEncoder),
        'data': json.dumps(data, cls=DjangoJSONEncoder),

        'labels2': json.dumps(labels2, cls=DjangoJSONEncoder),
        'data2': json.dumps(data2, cls=DjangoJSONEncoder),
    }
    return render(request,'master.html',context)

@login_required()
def search(request):
    if request.method == 'POST':
        searched = request.POST['search']
        stock = Stock.objects.filter(Q(inventory__name__contains=searched) | Q(unit__name__contains=searched))
        inventory = Inventory.objects.filter(Q(name__contains=searched) | Q(brand__name__contains=searched) | Q(subcategory__name__contains=searched))
        brand = Brand.objects.filter(name__icontains=searched)
        return render(request, 'search/search.html',{
        'title': 'Search',
        'searched': searched,
        'stock': stock,
        'inventory': inventory,
        'brand': brand,
    })
    else:
        return render(request, 'search/search.html',{
            'title': 'Search',
        })

# Auth
def login(request):
    context = {
        'title': 'Administration',
    }
    # if request.user.is_authenticated:
    #     return redirect('/admin/')
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/admin/')
        else:
            messages.error(request, 'Unauthorized to access the admin.')
            return redirect('shop:shop')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_superuser:
                    auth_login(request, user)
                    return redirect('/admin/')
                else:
                    messages.error(request, ('Unauthorized'))
                    return redirect('/admin/login/')
            else:
                messages.error(request, ('Invalid username or password'))
                return redirect('/admin/login/')
        else:
            return render(request,'login.html',context)

def logout(request):
    auth_logout(request)
    messages.success(request, ('Logout successful'))
    return redirect('/admin/login/')

def forgotPassword(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/admin/')
        else:
            messages.error(request, 'Unauthorized to access the admin.')
            return redirect('shop:shop')
    context = {
        'title': 'Forgot Password',
    }
    if request.method == 'POST':
        email = request.POST['email']
        try:
            users = User.objects.filter(email=email)
            if users.count() == 1:
                user = users.first()
                new_password_reset = PasswordReset(user=user)
                new_password_reset.save()
                reset_password_url = reverse('adminpanel:reset-password', kwargs={'reset_id': new_password_reset.reset_id})
                full_reset_password_url = f'{request.scheme}://{request.get_host()}{reset_password_url}'
                subject = 'You request reset password.'
                body = f'Here is the link of your reset password {user.first_name} {user.last_name}. \n{full_reset_password_url}'
                sender = settings.DEFAULT_FROM_EMAIL
                receiver = [email]
                message = EmailMessage(subject, body, sender, receiver)
                message.fail_silently = True
                message.send()
                return redirect(reverse('adminpanel:sent-reset-password', kwargs={'reset_id': new_password_reset.reset_id}))
            else:
                messages.error(request, 'Multiple emails found.')
                return redirect('/admin/forgot-password/')
        except User.DoesNotExist:
            messages.error(request, 'Email not found')
            return redirect('/admin/forgot-password/') 
    else:
        return render(request,'forgot-pass/forgot-password.html',context)

def sentResetPassword(request, reset_id):
    context = {
        'title': 'Sent Reset Password',
    }
    if PasswordReset.objects.filter(reset_id=reset_id).exists():
        return render(request,'sent-pass/sent-reset-password.html',context)
    else:  
        messages.error(request, 'Reset id not found')
        return redirect('/admin/forgot-password/')

def resetPassword(request, reset_id):
    context = {
        'title': 'Reset Password',
        'reset_id': reset_id,
    }
    try:
        reset_password_id = PasswordReset.objects.get(reset_id=reset_id)
        if request.method == 'POST':
            password = request.POST['password']
            confirm_password = request.POST['confirm-password']
            passwords_have_error = False
            if password != confirm_password:
                passwords_have_error = True
                messages.error(request, 'Passwords do not match')
            else:
                if len(password) < 5:
                    passwords_have_error = True
                    messages.error(request, 'Passwords is too short')
                else:
                    expiration_time = reset_password_id.created_when + timezone.timedelta(minutes=5)
                    if timezone.now() > expiration_time:
                        passwords_have_error = True
                        messages.error(request, 'Reset link has expired')
                    else:
                        if not passwords_have_error:
                            user = reset_password_id.user
                            user.set_password(password)
                            user.save()
                            reset_password_id.delete()
                            messages.error(request, 'Reset password successful')
                            return redirect('/admin/login/')  
    except PasswordReset.DoesNotExist:
        messages.error(request, 'Reset id not found')
        return redirect('/admin/forgot-password/')    
    return render(request,'reset-pass/reset-password.html',context)