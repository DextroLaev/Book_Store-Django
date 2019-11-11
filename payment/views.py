from django.shortcuts import render,redirect
from django.contrib import messages
from . models import Payment
from books.models import Books

# Create your views here.
def payment_gateway(request,product_id):
    product = Books.objects.get(id=product_id)
    return render(request,'payment/payment_gateway.html',{'product':product})

def buy(request,product_id,user_id):
    if request.method=='POST':
        if request.POST['name'] and request.POST['address'] and request.POST['city'] and request.POST['state'] and request.POST['zipcode'] and request.POST['phone']:
            user = Payment()
            user.name = request.POST['name']
            user.address = request.POST['address']
            user.city = request.POST['city']
            user.state = request.POST['state']
            user.zipcode = request.POST['zipcode']
            user.phone = request.POST['phone']
            user.product_id = product_id
            user.master_user_id = user_id
            if request.POST.get('debitcard','on'):
                if request.POST['cardno'] and request.POST['cardname'] and request.POST['carddate'] and request.POST['cardmonth']:  
                    user.payment_type = "Debit card/Credit card"
                    card_number = request.POST['cardno']
                    user.card_holder_name = request.POST['cardname']
                    user.card_day = request.POST['carddate']
                    user.card_month = request.POST['cardmonth']
                    for i in range(len(card_number)):
                        if i==0:
                            user.card_no += card_number[i]
                        elif i%4==0:
                            user.card_no += ' '
                            user.card_no += card_number[i]
                        else:
                            user.card_no += card_number[i]
                else:
                    messages.error(request,'Please fill all the card details.')
                    return redirect('home')                   
            else:
                user.payment_type = 'COD'

            user.save()
            return redirect('home')        
        else:
            messages.error(request,'please fill all the columns')
            return redirect('home')
           
