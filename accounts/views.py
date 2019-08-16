from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth,messages
from . models import Eligibility

# Create your views here.
def signup(request):
    if request.method=='POST':
       if request.POST['password1']==request.POST['password2']:
          if User.objects.filter(username=request.POST['username']).exists():
             messages.error(request,'Username is already taken')
             return render(request,'books/home.html')
          else:
             if User.objects.filter(email=request.POST['email']).exists():
                messages.error(request,'This gmail is already taken try another one')
                return render(request,'books/home.html')
                
             else:
                money = Eligibility()
                seller = request.POST.get('Seller','off')
                customer = request.POST.get('Customer','off')
                if seller == 'on':
                  if request.method == 'POST':
                     if int(request.POST['amount']) <= 700:
                        messages.error(request,'Not enough money')
                        return redirect('home')                        
                     else:
                        money.monthly_payment = int(request.POST['amount'])  
                        print('seller')
                else:
                  money.monthly_payment = 0
                  print('customer')
                money.save()  
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'],first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'])
                auth.login(request,user)
                if money.monthly_payment >= 700:
                   print(money.monthly_payment)
                   return redirect('home')
                  #  return render(request,'books/home.html',{'eligible':eligible_user})
                
       else:
          messages.error(request,'Passwords did not matched')
          return render(request,'books/home.html')
def login(request):
    if request.method=='POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
           auth.login(request,user)
           return redirect('home')
        else:
           messages.info(request,'Informations are incorrect')   
           return render(request,'books/home.html')
def logout(request):
        auth.logout(request)
        return redirect('home')

def forget(request):
   if request.method=='POST':
      try:
         user = User.objects.get(username=request.POST['username'],email=request.POST['email'],first_name=request.POST['first_name'])
         user.set_password(request.POST['change_password'])
         user.save()
         return redirect('home')
      except User.DoesNotExist:
         return render(request,'accounts/forget.html',{'error':'The given informations are not correct!!'})
   else:
      return render(request,'accounts/forget.html')        


        
     
        
