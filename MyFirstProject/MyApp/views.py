from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")


def myLogin(request):
    return render(request,"login.html")

def mySignup(request):
    return render(request,"signup.html")


def myLogout(request):
    return render(request,"logout")