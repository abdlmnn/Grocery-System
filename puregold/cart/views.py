from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def cart(request):
    customer = request.user.customer
    cart_items = Cartline.objects.filter(cart__customer=customer)
    return render(request, 'cart.html', {
        'cart_items': cart_items,
    })

def add_to_cart(request, stock_id):
    customer = request.user.customer
    cart, created = Cart.objects.get_or_create(customer=customer, status='active')
    stock = get_object_or_404(Stock, id=stock_id)

    cartline, created = Cartline.objects.get_or_create(cart=cart, stock=stock)
    
    if created:
        cartline.quantity = 1
    else:
        # Check if there’s still stock available to add
        if stock.quantity < (cartline.quantity + 1):
            return redirect('shop:shop')

        cartline.quantity += 1

    cartline.save()

    stock.quantity -= 1
    stock.save()

    return redirect('cart:car')  

def delete(request, id):
    cart_line = get_object_or_404(Cartline, id=id, cart__customer=request.user.customer)
    cart_line.delete()
    return redirect('cart:cart')