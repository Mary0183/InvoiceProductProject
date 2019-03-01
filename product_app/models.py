import datetime

from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6 , decimal_places=2)
    
    def __str__(self):
        return self.product_name

class Invoice(models.Model):
    purchase_date = models.DateTimeField()
    total_invoice = models.DecimalField(max_digits=7 , decimal_places=2)
    products = models.ManyToManyField(Product, through='Invoice_Product')
    
    def __str__(self):
        return self.purchase_date.strftime("%Y-%m-%d %H:%M:%S")

class Invoice_Product(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7 , decimal_places=2)
    quantity = models.IntegerField()    

