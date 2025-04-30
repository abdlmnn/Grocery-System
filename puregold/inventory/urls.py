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
    path('viewstock/<int:pID>/',viewStock,name='viewStock'),
    path('editstock/<int:pID>/',editStock,name='editStock'),
    path('deletestock/<int:pID>/',deleteStock,name='deleteStock'),


    path('addcategory/',addCategory,name='addCategory'),
    path('viewcategory/<int:cID>/',viewCategory,name='viewCategory'),
    path('editcategory/<int:cID>/',editCategory,name='editCategory'),
    path('deletecategory/<int:cID>/',deleteCategory,name='deleteCategory'),


    path('addsubcategory/',addSubCategory,name='addSubCategory'),
    path('viewsubcategory/<int:sID>/',viewSubCategory,name='viewSubCategory'),
    path('editsubcategory/<int:sID>/',editSubCategory,name='editSubCategory'),
    path('deletesubcategory/<int:sID>/',deleteSubCategory,name='deleteSubCategory'),
] 
