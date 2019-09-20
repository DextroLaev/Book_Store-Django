from django.db import models

# Create your models here.
class Payment(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=60)
    zipcode = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    payment_type = models.CharField(max_length=20)

    def __str__(self):
        
        return self.name + '({})'.format(self.id)
        