from django.shortcuts import render
from . models import *
# Create your views here.

def home(request):
    id = request.GET.get('q')
    if(id==None):
        id = ""
    print(id)
    categories = Category.objects.all()
    posts = Post.objects.filter(category__id__icontains=id)
    context={
        'categories':categories,
        'posts':posts,
    }
    return render(request,'home.html',context)

def userLogin(request):
    context={}
    return render(request,'login.html',context)

def userLogout(request):
    context={}
    return render(request, 'logout.html',context)

def userRegister(request):
    context={}
    return render(request,'register.html',context)

def post(request):
    context={}
    return render(request, 'post.html',context)

