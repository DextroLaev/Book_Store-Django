from django.db import models

# Create your models here.
class Payment(models.Model):
    phone_pay = models.IntegerField(default=0)
    paytm = models.IntegerField(default=0)
    
    card_holder_name = models.CharField(max_length=60,default='None')
    card_no = models.CharField(max_length=21,default='None')
    product_id= models.IntegerField(default=0)
    master_user_id = models.IntegerField(default=0)
    card_day = models.IntegerField(default=0)
    card_month = models.IntegerField(default=0)
    payment_type = models.CharField(max_length=20)

    def __str__(self):
        
        return "user id:-" + '({})'.format(self.id)
        

class To_order(models.Model):
    product_to_order_id = models.IntegerField()
    master_user_id = models.IntegerField(default=0)

    def __str__(self):
        return "user id:- " + '({})'.format(self.id)     
