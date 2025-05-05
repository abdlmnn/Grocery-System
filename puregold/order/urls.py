from django.urls import path
from .views import *

urlpatterns = [
    # Main
     path('', all_orders, name='all-orders'),
     path('place/', placed_orders, name='place'),
     path('processing/', processing_orders, name='processing-orders'),
     path('delivered/', delivered_orders, name='delivered-orders'),
     path('cancelled/', cancelled_orders, name='cancelled-orders'),
     path('<int:id>/update-status/', update_order_status, name='update-status'),


    path('place-order/', place_order, name='place-order'),
    path('invoice/<int:id>/', invoice, name='invoice'),
    path('history/', order_history, name='history'),
    path('thank-you/',thank_you,name='thank-you'),
] 
