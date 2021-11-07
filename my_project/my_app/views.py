from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from .models import *

# Create your views here.

def index(request):
    posts= Post.objects.all()
    context={
        'posts':posts,
    }
    return render(request,"index.html",context)


def userLogin(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

        else:
            print("User is not register")
            return render(request,"login.html")

        print(username)
        print(password)
    return render(request,"login.html")

def userLogout(request):
    return render(request,"logout.html")

def userSignup(request):
    return render(request,"signup.html")
