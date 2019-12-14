from django.urls import path,include
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name='home'),
    path('orders/<int:user_id>',views.orders,name='orders'),
    path('cart/',views.cart,name='cart'),
    path('about/',views.about,name='about'),
    path('service/',views.service,name='service'),
    path('addproducts/',views.addproducts,name='addproducts'),
    path('delete_product/<int:delete_id>',views.delete,name='delete_product')
   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

