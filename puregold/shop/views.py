from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from inventory.models import *

# Create your views here.

def shop(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('/admin/')
    context = {
        'stocks': Stock.objects.all(),
        'category': Category.objects.all(),
        'subcategory': Subcategory.objects.all(),
        'brand': Brand.objects.all(),
    }
    return render(request,'shop.html', context)

def login(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('/admin/')
    if request.user.is_authenticated:
        return redirect('shop:shop')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                if user.is_superuser or user.is_staff:
                    messages.error(request, 'Unauthorized.')
                    return redirect('shop:login')
                auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend') 
                return redirect('shop:shop')  
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('shop:login') 
        except User.DoesNotExist:
            messages.error(request, 'Invalid email address')
            return redirect('shop:login')
    return render(request,'content/login.html')

def logout(request):
    auth_logout(request)
    messages.success(request, ('Logout successful'))
    return redirect('shop:login')

def register(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('/admin/')
    if request.user.is_authenticated:
        return redirect('shop:shop')
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        passwords_have_error = False
        if password1 != password2:
            passwords_have_error = True
            messages.error(request, 'Passwords do not match')
        else:
            if len(password1) < 5:
                    passwords_have_error = True
                    messages.error(request, 'Passwords is too short')
            else:
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'Username already taken')
                    return render(request, 'content/register.html')
                else:
                    user = User.objects.create_user(
                        first_name = first_name,
                        last_name = last_name,
                        email = email,
                        username = username,
                        password = password1
                    )
                    user.is_superuser = False
                    user.is_staff = False
                    user.save()
                    auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    
                    return redirect('shop:shop') 
    context = {
        'hi': 'hi'
    }
    return render(request,'content/register.html', context)