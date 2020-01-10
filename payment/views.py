from django.shortcuts import render,redirect
from django.contrib import messages
from . models import Payment,To_order
from books.models import Books

# Create your views here.
def payment_gateway(request,product_id):
    product = Books.objects.get(id=product_id)
    return render(request,'payment/payment_gateway.html',{'product':product})

def buy(request,product_id,user_id):
    if request.method=='POST':
        debit = request.POST.get('debitcard','off')
        cash_on_delivery = request.POST.get('cod','off')
        paytm = request.POST.get('paytm','off')
        phone_pay = request.POST.get('phonepay','off')

        user = Payment()
        user.product_id = product_id
        user.master_user_id = user_id
        if debit=='on':
            if request.POST['cardno']!=None and request.POST['cardname']!=None and request.POST['carddate']!=None and request.POST['cardmonth']!=None:  
                user.payment_type = "Debit card/Credit card"
                card_number_data = request.POST['cardno']
                user.card_holder_name = request.POST['cardname']
                user.card_day = request.POST['carddate']
                user.card_month = request.POST['cardmonth']
                for i in range(len(card_number_data)):
                    if i==0:
                        user.card_no += card_number_data[i]
                    elif i%4==0:
                        user.card_no += ' '
                        user.card_no += card_number_data[i]                      
                    else:
                        user.card_no += card_number_data[i]
                                       
            else:
                messages.error(request,'Please fill all the card details.')
                return redirect('home')                   
        elif paytm=='on':
            user.payment_type='Paytm'
            user.paytm = int(request.POST['phone_no_paytm'])
            print(user.payment_type)
        elif phone_pay=='on':
            user.payment_type = 'Phonepay'    
            user.phone_pay = int(request.POST['phone_no_phonepay'])
            print(user.payment_type)
        elif cash_on_delivery=='on':
            user.payment_type = 'COD'    
            print(user.payment_type)

        user.save()
        return redirect('home')        
    else:
        messages.error(request,'please fill all the columns')
        return redirect('home')

def add_cart(request,product_id):
    cart = To_order()
    cart.product_to_order_id = product_id
    cart.save()
    return redirect('home')