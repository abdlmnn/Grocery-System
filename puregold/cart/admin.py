from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Cart)
class Cart(admin.ModelAdmin):
    list_display = ('customer','status',)
    search_fields = ('customer','status',)

@admin.register(Cartline)
class Cartline(admin.ModelAdmin):
    list_display = ('cart','stock', 'quantity', 'total_amount',)
    search_fields = ('cart','stock', 'quantity', 'total_amount',)