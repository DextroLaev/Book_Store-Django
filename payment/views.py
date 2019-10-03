from django.shortcuts import render,redirect
from . models import Payment
from books.models import Books

# Create your views here.
def payment_gateway(request,product_id):
    product = Books.objects.get(id=product_id)
    return render(request,'payment/payment_gateway.html',{'product':product})

def buy(request,product_id):
    if request.method=='POST':
        user = Payment()
        user.name = request.POST['name']
        user.address = request.POST['address']
        user.city = request.POST['city']
        user.state = request.POST['state']
        user.zipcode = request.POST['zipcode']
        user.phone = request.POST['phone']
        user.card_holder_name = request.POST['cardname']
        user.card_day = request.POST['carddate']
        user.card_month = request.POST['cardmonth']
        user.product_id = product_id
        if request.POST.get('debitcard','on'):
            user.payment_type = "Debit card/Credit card"
            card_number = request.POST['cardno']
            for i in range(len(card_number)):
                if i==0:
                    user.card_no += card_number[i]
                elif i%4==0:
                    user.card_no += ' '
                    user.card_no += card_number[i]
                else:
                    user.card_no += card_number[i]        
                    
        else:
            user.payment_type = 'COD'

        user.save()
        return redirect('home')        