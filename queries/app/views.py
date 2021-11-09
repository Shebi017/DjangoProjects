from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello everyone My boss called me as i was completing your project..")