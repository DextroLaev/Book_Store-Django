from django.db import models

# Create your models here.
class Payment(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=60)
    zipcode = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    card_holder_name = models.CharField(max_length=60)
    card_no = models.CharField(max_length=21)
    product_id= models.IntegerField(default=0)
    master_user_id = models.IntegerField(default=0)
    card_day = models.IntegerField(default=0)
    card_month = models.IntegerField(default=0)
    payment_type = models.CharField(max_length=20)

    def __str__(self):
        
        return self.name + '({})'.format(self.id)
        