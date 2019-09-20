
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('payment_gateway/',views.payment_gateway,name='payment_gateway'),
    path('buy/',views.buy,name='buy')
]
