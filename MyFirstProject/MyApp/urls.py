from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('login',views.myLogin,name="myLogin"),
    path('signup',views.mySignup,name="mySignup"),
    path('logout',views.myLogout,name="myLogout"),
]
