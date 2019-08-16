from django.shortcuts import render,redirect
from . models import Books
from accounts.models import Eligibility

# Create your views here.



# Create your views here.
def home(request):
    money = Eligibility.objects.all()
    money = money[1].monthly_payment
    # items = Books.objects.all()
    return render(request,'books/home.html',{'money':money})

def orders(request):
    return render(request,'books/orders.html')    

def cart(request):
    return render(request,'books/cart.html')    

def about(request):
    return render(request,'books/about.html')

def service(request):
    return render(request,'books/service.html')




    
    
