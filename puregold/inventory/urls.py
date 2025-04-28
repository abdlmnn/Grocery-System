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

    # CRUD
    path('addproduct/',addProduct,name='addProduct'),
    path('viewproduct/<int:pID>/',viewProduct,name='viewProduct'),
    path('editproduct/<int:pID>/',editProduct,name='editProduct'),
    path('deleteproduct/<int:pID>/',deleteProduct,name='deleteProduct'),


    path('addstock/',addStock,name='addStock'),
    path('getimage/<int:pID>/',getImage,name='getImage'),
] 
