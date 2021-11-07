from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=True,blank=True)
    email = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.user.username
    

class GenderCategory(models.Model):
    genderName = models.CharField(max_length=50)

    def __str__(self):
        return self.genderName
    

class ProductCategory(models.Model):
    productName = models.CharField(max_length=50)

    def __str__(self):
        return self.productName
    

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.ImageField(upload_to="images/products")
    genderCategory = models.ForeignKey(GenderCategory,on_delete=models.CASCADE) 
    productCategory = models.ForeignKey(ProductCategory,on_delete=models.CASCADE) 
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    


class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return str(self.id)
    



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True,default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
    


class ShippingAdress(models.Model):
    customer =  models.ForeignKey(Customer,on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    city= models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.name+"   "+ order.id
    


    


