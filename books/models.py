from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Books(models.Model):
    Name = models.TextField()
    publisher = models.CharField(max_length=50)
    book_language = models.CharField(max_length=50)
    descreption = models.CharField(max_length=300)
    edition = models.CharField(max_length=20)
    ISBN = models.IntegerField()
    pages = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField(default=1)
    #hunter = models.CharField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.Name + '({})'.format(self.id)