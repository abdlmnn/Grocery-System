from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    # Main
    path('',shop,name="shop"),
    path('login/',login,name="login"),
    path('logout/',logout,name="logout"),
    path('register/',register,name="register"),
] 
