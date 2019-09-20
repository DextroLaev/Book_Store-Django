from django.shortcuts import render,redirect
from . models import Payment


# Create your views here.
def payment_gateway(request):
    return render(request,'payment/payment_gateway.html')

def buy(request):
    if request.method=='POST':
        user = Payment()
        user.name = request.POST['name']
        user.address = request.POST['address']
        user.city = request.POST['city']
        user.state = request.POST['state']
        user.zipcode = request.POST['zipcode']
        user.phone = request.POST['phone']
        if request.POST.get('debitcard','on'):
            user.payment_type = "Debit card/Credit card"
        else:
            user.payment_type = 'COD'

        user.save()
        return redirect('home')        