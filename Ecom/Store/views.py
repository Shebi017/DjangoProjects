from django.shortcuts import render
from django.db.models import Q  
from django.http import JsonResponse
import json
from . models import *
# Create your views here.

def home(request):
    q = request.GET.get('q')
    if q is not None:
        q = request.GET.get('q')
        print("The value of q is : " , q)

    else:
        q = ""
        print("The value of q is : " , q)
    products = Product.objects.filter(
        Q(genderCategory__id__icontains= q) |
        Q(name__icontains= q)|
        Q(productCategory__productName__icontains= q)
    )
    gcategories = GenderCategory.objects.all()
    context={
        'products':products,
        'gcategories':gcategories,
    }
    return render(request,"home.html",context)


def cart(request):
    customer=request.user.customer
    order = Order.objects.get(customer=customer)  
    items = order.orderitem_set.all()

    context={
        'items':items,
    }
    return render(request,"cart.html",context)

def updatecart(request):
    if request.method == "POST":
        data = json.loads(request.body)
        ####### Data From FrontEnd  ###########
        product_id = data.get('product_id')
        product = Product.objects.get(id=product_id)
        user = request.user
        customer,created = Customer.objects.get_or_create(user=user)       
        action = data.get('action')
        #######################################
        print(product_id)
        print(customer)
        print(created)
        print(action)
        ### Now Create or Get Order #######
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        print(order)
        print(created)
        orderitem,createditem = OrderItem.objects.get_or_create(order=order,product=product)
        if action=="add":
            orderitem.quantity = (orderitem.quantity +1)
        else:
            orderitem.quantity = (orderitem.quantity -1)
        if orderitem.quantity <=0:
            orderitem.delete()
        orderitem.save()
        print(orderitem)
        print(createditem)
        return JsonResponse("Data is received successfully",safe=False)
    return JsonResponse("Update Page !",safe=False)

def checkout(request):
    return render(request,"checkout.html")

def userlogin(request):
    return render(request,"login.html")

def userlogout(request):
    return render(request,"logout.html")

def userregister(request):
    return render(request,"register.html")
