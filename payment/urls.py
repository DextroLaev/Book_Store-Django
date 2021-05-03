
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('payment_gateway/<int:product_id>/',views.payment_gateway,name='payment_gateway'),
    path('buy/<int:product_id>/<int:user_id>/',views.buy,name='buy'),
    path('add_cart/<int:product_id>/<int:user_id>/',views.add_cart,name='add_cart')
   
]
