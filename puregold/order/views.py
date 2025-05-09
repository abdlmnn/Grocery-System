from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from cart.models import Cart, Cartline
from .models import *
from inventory.models import Stock  
from accounts.models import Customer  
from django.contrib import messages
from payment.models import Payment
from datetime import datetime
from notification.models import Notification
from django.contrib.auth.models import User

@login_required
def cancelled_orders(request):
    orders = Order.objects.filter(status='cancelled').order_by('-id')
    return render(request, 'cancelled-orders.html', {
        'orders': orders,
        'title': 'Cancelled Orders',
        'button': 'Orders',
    })

@login_required
def delivered_orders(request):
    orders = Order.objects.filter(status='completed').order_by('-id')
    return render(request, 'delivered-orders.html', {
        'orders': orders,
        'title': 'Delivered Orders',
        'button': 'Orders',
    })

@login_required
def placed_orders(request):
    orders = Order.objects.filter(status='pending').order_by('-id')
    return render(request, 'place.html', {
        'orders': orders,
        'title': 'Placed Orders',
        'button': 'Orders',
    })

@login_required
def processing_orders(request):
    orders = Order.objects.filter(status='processing').order_by('-id')
    return render(request, 'processing-orders.html', {
        'orders': orders,
        'title': 'Processing Orders',
        'button': 'Orders',
    })
    

@login_required
def update_order_status(request, id):
    if request.method == 'POST':
        order = get_object_or_404(Order, id=id)
        old_status = order.status
        new_status = request.POST.get('status')
        if new_status in dict(Order.STATUS_CHOICES):
            order.status = new_status
            order.save()
            if old_status != new_status:
                Notification.objects.create(
                    user=order.customer.user,
                    title=f"Order Status #{order.id}",
                    message=f"Your order #{order.id} status changed from {old_status} to {new_status}.",
                    order=order
                )
        else:
            messages.error(request, "Invalid status selected.")
    return redirect(request.META.get('HTTP_REFERER', 'order:all-orders'))

@login_required
def all_orders(request):
    orders = Order.objects.all().select_related('customer').prefetch_related('orderline_set').order_by('-id')
    for order in orders:
        if order.status != 'pending' and not Notification.objects.filter(user=order.customer.user, order=order, title__icontains='Status').exists():
            Notification.objects.create(
                user=order.customer.user,
                title=f"Order Status #{order.id}",
                message=f"Your order #{order.id} is currently {order.get_status_display().lower()}.",
                order=order
            )
    context = {
        'button': 'Orders',
        'title': 'All Orders',
        'orders': orders
    }
    return render(request, 'all-orders.html', context)

@login_required(login_url='/login/')
@transaction.atomic
def place_order(request):
    customer = request.user.customer
    cart_items = Cartline.objects.filter(cart__customer=customer)

    if request.method == "POST":
        phone_number = request.POST.get('phone_number')
        birth_raw = request.POST.get('birth')
        payment_method = request.POST.get('payment_method')
        address = request.POST.get('address')
        if birth_raw:
            try:
                birth = datetime.strptime(birth_raw, "%Y-%m-%d").date()
                customer.birth = birth
            except ValueError:
                return redirect('cart:checkout')
        customer.phone_number = phone_number
        customer.address = address
        customer.save()
        if not cart_items.exists():
            messages.error(request, "Your cart is empty!")
            return redirect('cart:cart')
        order = Order.objects.create(
            customer=customer
        )
        Notification.objects.create(
            user=customer.user,
            title=f"Order Placed #{order.id}",
            message=f"Your order (ID: {order.id}) has been placed successfully. We’ll notify you once it’s processed."
        )
        admin_users = User.objects.filter(is_superuser=True)
        for admin in admin_users:
            Notification.objects.create(
                user=admin,
                title=f"New Order Received",
                message=f"New order (Order ID: {order.id}) placed by {customer.user.get_full_name()}."
            )
        for cart_item in cart_items:
            Orderline.objects.create(
                order=order,
                stock=cart_item.stock,
                quantity=cart_item.quantity,
                total_amount=cart_item.total_amount
            )
        cart_items.delete()
        if payment_method == 'cod':
            Payment.objects.create(
                customer=customer,
                order=order,
                method='cod',
                status='pending'
            )
            return redirect('order:invoice', id=order.id)
        elif payment_method == 'gcash':
            payment = Payment.objects.create(
                customer=customer,
                order=order,
                method='gcash',
                status='pending'
            )
            return redirect('payment:gcash', id=payment.id)
        return redirect('order:thank-you')
    return redirect('cart:checkout')

def invoice(request, id):
    order = get_object_or_404(Order, id=id, customer=request.user.customer)
    return render(request, 'invoice.html', {'order': order})


@login_required(login_url='/login/')
def order_history(request):
    orders = Order.objects.filter(customer__user=request.user).order_by('-id')
    return render(request, 'orders/order_history.html', {'orders': orders})

@login_required(login_url='/login/')
def thank_you(request):
    return render(request, 'thank-you.html')