from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('orders/',views.orders,name='orders'),
    path('cart/',views.cart,name='cart'),
    path('about/',views.about,name='about'),
    path('service/',views.service,name='service'),
    path('addproducts/',views.addproducts,name='addproducts')
   
]
