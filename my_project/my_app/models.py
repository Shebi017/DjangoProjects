from django.db import models


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to="images")
    mychoices =[
        ('Sports','Sports'),
        ('Entertainment','Entertainment'),
        ('Politics','Politics'),
        ('Technology','Technology')
    ]

    category = models.CharField( max_length=50,choices=mychoices,default="")


    def __str__(self):
        return self.title
    