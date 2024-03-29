from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    choices = [
        ('Laptop','Laptop'),
        ('Mobile','Mobile'),
    ]
    category = models.CharField(max_length=50,choices=choices)

    def __str__(self):
        return self.name
    


class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    date_orderd =models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)
    

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)