from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from wishlist.models import Wishlist
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def checkout(request):
    cart_items = Cartline.objects.filter(cart__customer=request.user.customer)
    total_price = sum(item.total_amount for item in cart_items)
    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })



@login_required(login_url='/login/')
def cart(request):
    customer = request.user.customer
    cart_items = Cartline.objects.filter(cart__customer=customer)
    total_price = sum(item.total_amount for item in cart_items)
    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })

@login_required(login_url='/login/')
def add_to_cart(request, stock_id):
    customer = request.user.customer
    cart, created = Cart.objects.get_or_create(customer=customer, status='active')
    stock = get_object_or_404(Stock, id=stock_id)
    cartline, created = Cartline.objects.get_or_create(cart=cart, stock=stock)
    if created:
        cartline.quantity = 1
        stock.quantity -= 1 
    else:
        cartline.quantity += 1
        stock.quantity -= 1
    cartline.save()
    stock.save()
    Wishlist.objects.filter(customer=customer, stock=stock).delete()
    return redirect('shop:shop')

@login_required(login_url='/login/')
def update_quantity(request, id):
    cartline = get_object_or_404(Cartline, id=id)
    if request.method == "POST":
        try:
            new_qty = int(request.POST.get("quantity"))
            if new_qty <= 0:
                return redirect('cart:cart')

            stock = cartline.stock
            stock.quantity += cartline.quantity  # Restore old quantity
            if stock.quantity < new_qty:
                return redirect('cart:cart')

            cartline.quantity = new_qty
            stock.quantity -= new_qty
            cartline.total_amount = stock.price * new_qty
            cartline.save()
            stock.save()
        except Exception as e:
            print('Error')
    return redirect('cart:cart')

@login_required(login_url='/login/')
def delete(request, id):
    cart_line = get_object_or_404(Cartline, id=id, cart__customer=request.user.customer)
    stock = cart_line.stock
    stock.quantity += cart_line.quantity
    stock.save()
    cart_line.delete()
    return redirect('cart:cart')