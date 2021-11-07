from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=150)
    price = models.IntegerField()
    img = models.ImageField(upload_to="images/product/")


    def __str__(self):
        return self.name
    

