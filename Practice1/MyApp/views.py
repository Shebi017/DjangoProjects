from django.shortcuts import render
from MyApp.models import *

# Create your views here.

def index(request):
    posts = Post.objects.all()
    context={
        'posts':posts,
    }
    return render(request,"index.html",context)


def userLogin(request):
    return render(request,"login.html")

def userLogout(request):
    return render(request,"logout.html")

def userRegister(request):
    return render(request,"register.html")