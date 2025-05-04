from django.shortcuts import redirect, get_object_or_404, render
from .models import Wishlist
from inventory.models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def wishlist(request):
    customer = request.user.customer
    wishlist_items = Wishlist.objects.filter(customer=customer).select_related('stock__inventory', 'stock__inventory__subcategory__category')
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})

@login_required(login_url='/login/')
def add_to_wishlist(request, stock_id):
    if request.user.is_authenticated:
        customer = request.user.customer 
        stock = get_object_or_404(Stock, id=stock_id)
        Wishlist.objects.get_or_create(customer=customer, stock=stock)
        return redirect('shop:shop')  
    else:
        return redirect('shop"login')
    
@login_required(login_url='/login/')
def delete(request, id):
    wishlist_item = get_object_or_404(Wishlist, id=id)
    wishlist_item.delete()
    return redirect('wishlist:wishlist')