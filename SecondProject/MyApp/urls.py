from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('login',views.usersignin,name="usersignin"),
    path('logout',views.userlogout,name="userlogout"),
    path('register',views.userregister,name="userregister"),
]