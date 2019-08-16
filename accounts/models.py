from django.db import models

# Create your models here.
class Eligibility(models.Model):

    monthly_payment = models.IntegerField(default=0)