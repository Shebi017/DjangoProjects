from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('login',views.userlogin,name="login"),
    path('register',views.userregister,name="register"),
    path('logout',views.userlogout,name="logout"),
    path('cart',views.cart,name="cart"),
    path('checkout',views.checkout,name="checkout"),
]