from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('cart',views.cart,name="cart"),
    path('checkout',views.checkout,name="checkout"),
    path('login',views.userLogin,name="login"),
    path('register',views.userRegister,name="register"),
]