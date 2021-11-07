from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Author(models.Model):
    personalinfo = models.OneToOneField( User,on_delete=models.CASCADE)

    def __str__(self):
        return self.personalinfo.username
    

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    date_publish = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title
    
