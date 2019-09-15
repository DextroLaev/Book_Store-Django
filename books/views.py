from django.shortcuts import render,redirect
from . models import Books
from django.contrib import messages
from accounts.models import Eligibility

# Create your views here.



# Create your views here.
def home(request):
   
    return render(request,'books/home.html')

def orders(request):
    return render(request,'books/orders.html')    

def cart(request):
    return render(request,'books/cart.html')    

def about(request):
    return render(request,'books/about.html')

def service(request):
    return render(request,'books/service.html')

def addproducts(request):
    products = Books()
    if request.method == 'POST':
        if request.POST['Name'] and request.POST['publisher'] and request.POST['author'] and request.POST['edition'] and request.POST['ISBN'] and request.POST['Language'] and request.POST['pages'] and request.POST['price'] and request.FILES['image']:
            products.Name = request.POST['Name']
            products.publisher = request.POST['publisher']
            products.book_language = request.POST['Language']
            products.edition = request.POST['edition']
            products.ISBN = request.POST['ISBN']
            products.pages = request.POST['pages']
            products.author = request.POST['author']
            products.price = request.POST['price']
            products.image = request.FILES['image']
            products.save()
            return redirect('home')
        else:
            messages.error(request,'Please fill all the details')
            return render(request,'books/home.html')
    else:
        return render(request,'books/create.html')        


    
    
