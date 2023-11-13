from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name
class Product(models.Model):
    name=models.CharField(max_length=200,null=True)
    price=models.FloatField()
    digital=models.BooleanField(default=False,null=True,blank=False)
    image_path = models.CharField(max_length=255, null=True, blank=False)
    #image=models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.name

class Order(models.Model):
    customer=models.ForeignKey(Customer ,on_delete=models.SET_NULL,blank=True,null=True)
    data_orderd=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False,null=True,blank=False)
    transaction_id=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class Order_Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    data_added = models.DateTimeField(auto_now_add=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)

class shippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address=models.CharField(max_length=200,null=True)
    city=models.CharField(max_length=200,null=True)
    state=models.CharField(max_length=200,null=True)
    pincode=models.CharField(max_length=200,null=True)
    data_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
# Create your models here.
