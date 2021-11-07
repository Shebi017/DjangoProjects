from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login',views.userLogin,name="login"),
    path('logout',views.userLogout,name="logout"),
    path('register',views.userRegister,name="register"),
    path('post',views.post,name="post"),
]