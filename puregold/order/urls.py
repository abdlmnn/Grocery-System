from django.urls import path
from .views import *

urlpatterns = [
    # Main
    path('place-order/', place_order, name='place-order'),
    path('invoice/<int:id>/', invoice, name='invoice'),
    path('history/', order_history, name='history'),
    path('thank-you/',thank_you,name='thank-you'),
] 
