from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index.html'),
    path('login', views.loginUser, name='login.html'),
    path('logout', views.logoutUser, name='logout.html'),
    path('signup', views.signupUser, name='signup.html')
]
