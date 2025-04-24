from django.urls import path
from .views import *

urlpatterns = [
    # Main
    path('',product,name='product'),
    path('stocks/',stock,name='stock'),
    path('categories/',category,name='category'),
    path('subcategories/',subcategory,name='subcategory'),
    path('brands/',brand,name='brand'),
    path('units/',unit,name='unit'),
] 
