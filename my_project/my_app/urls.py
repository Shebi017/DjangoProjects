from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("all",views.index,name="all"),
    path("login",views.userLogin,name="login"),
    path("logout",views.userLogout,name="logout"),
    path("signup",views.userSignup,name="signup"), 
]