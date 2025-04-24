from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('name','created_date')
    search_fields = ('name','created_date')
    list_filter = ('name','created_date')

@admin.register(Subcategory)
class Subcategory(admin.ModelAdmin):
    list_display = ('category','name','created_date')
    search_fields = ('category','name','created_date')
    list_filter = ('category','name','created_date')

@admin.register(Brand)
class Brand(admin.ModelAdmin):
    list_display = ('name','created_date')
    search_fields = ('name','created_date')
    list_filter = ('name','created_date')

@admin.register(Unit)
class Unit(admin.ModelAdmin):
    list_display = ('name','abbreviation','created_date')
    search_fields = ('name','abbreviation','created_date')
    list_filter = ('name','abbreviation','created_date')

@admin.register(Inventory)
class Inventory(admin.ModelAdmin):
    list_display = ('subcategory','brand','name','created_date')
    search_fields = ('subcategory','brand','name','created_date')
    list_filter = ('subcategory','brand','name','created_date')

@admin.register(Stock)
class Stock(admin.ModelAdmin):
    list_display = ('inventory','quantity','amount_per_unit','unit','price', 'status', 'expiry_date','date_added')
    search_fields = ('inventory','quantity','amount_per_unit','unit','price', 'status', 'expiry_date', 'date_added')
    list_filter = ('inventory','quantity','amount_per_unit','unit','price', 'status', 'expiry_date', 'date_added')

