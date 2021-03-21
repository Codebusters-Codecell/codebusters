from django.db import models


# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=45)
    hid = models.CharField(max_length=45)
    country= models.CharField(max_length=45)
    state= models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    contact = models.CharField(max_length=10)
    count= models.CharField(max_length=10,default ='')
    email = models.EmailField()
    address = models.TextField()