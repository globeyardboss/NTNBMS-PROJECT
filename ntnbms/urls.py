from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views




urlpatterns = [


    url(r'^getdata/', views.new),


]



urlpatterns = [
    path('', views.login, name='login'),
    path('ntnbms/home', views.home, name='home'),
]