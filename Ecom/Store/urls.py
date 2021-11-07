from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('cart',views.cart,name="cart"),
    path('checkout',views.checkout,name="checkout"),
    path('update',views.updatecart,name="update"),
    path('login',views.userlogin,name="login"),
    path('logout',views.userlogout,name="logout"),
    path('register',views.userregister,name="register"),
]