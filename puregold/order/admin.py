from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ('customer','total_amount','status',)
    search_fields = ('customer','total_amount','status',)

@admin.register(Orderline)
class Orderline(admin.ModelAdmin):
    list_display = ('order','stock', 'quantity', 'total_amount',)
    search_fields = ('order','stock', 'quantity', 'total_amount',)