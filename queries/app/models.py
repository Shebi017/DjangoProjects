from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField( max_length=50)

    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField( max_length=50)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField( max_length=50)

    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
    
