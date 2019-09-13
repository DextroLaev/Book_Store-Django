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
        print(request.POST['language'])
        print('Successfull')
        if request.POST['Name']!=None and request.POST['publisher']!=None and request.POST['language']!=None and request.POST['edition']!=None and request.POST['ISBN']!=None and request.POST['Language']!=None and request.POST['pages']!=None and request.POST['price']!=None and request.POST['Image']!=None:
            products.name = request.POST['Name']
            products.publisher = request.POST['publisher']
            
            products.edition = request.POST['edition']
            products.ISBN = request.POST['ISBN']
            products.pages = request.POST['pages']
            products.author = request.POST['author']
            products.price = request.POST['price']
            products.image = request.FILES['Image']
            products.save()
            return redirect('home')
        else:
            messages.error(request,'Please fill all the details')
            return render(request,'books/home.html')
    else:
        return render(request,'books/create.html')        


    
    
