from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth import logout



# Create your views here.  username = shebi  , password = pakhwal1$


def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,"index.html")

def usersignin(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("***********************************")
        print(username)
        print(password)
        print("***********************************")
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('/')
        else:
            return render(request,"userlogin.html")

    return render(request,"userlogin.html")

def userlogout(request):
    if request.method=="POST":
        logout(request)
        return redirect("/login")
    return render(request,"userlogout.html")

def userregister(request):
    return render(request,"userregister.html")