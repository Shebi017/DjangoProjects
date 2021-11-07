from django.db import models
from datetime import datetime
# Create your models here.

class Post(models.Model):
    img = models.ImageField(upload_to="uploadimg")
    title = models.CharField(max_length=50)
    detail = models.CharField(max_length=150)
    date =  models.DateTimeField(auto_now=False, auto_now_add=False)
    CHOICES = [
        ('IT', 'IT'),
        ('Sports', 'Sports'),
        ('National', 'National'),   
    ]
    choice = models.CharField(max_length=50,choices=CHOICES,default="")

    def __str__(self):
        return self.title
    
