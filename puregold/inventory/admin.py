from django.contrib import admin
from .models import (
    Category,
    Subcategory,
    Brand,
    Unit,
    Inventory,
)

# Register your models here.
@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Subcategory)
class Subcategory(admin.ModelAdmin):
    list_display = ('category','name')
    search_fields = ('category','name')

@admin.register(Brand)
class Brand(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Unit)
class Unit(admin.ModelAdmin):
    list_display = ('name','abbreviation')
    search_fields = ('name','abbreviation')

@admin.register(Inventory)
class Inventory(admin.ModelAdmin):
    list_display = ('subcategory','brand','product_name','price','stock_quantity','unit_type','status','expiry_date')
    search_fields = ('subcategory','brand','product_name','price','stock_quantity','unit_type','status','expiry_date')