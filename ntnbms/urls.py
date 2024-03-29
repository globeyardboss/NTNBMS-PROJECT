from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views




urlpatterns = [


    url(r'^getdata/', views.new),
    url(r'^getdata/', views.newCustomer),
    

]



urlpatterns = [
    path('', views.login, name='login'),
    path('ntnbms/home', views.home, name='home'),
    path('ntnbms/viewCustomer', views.viewCustomer, name='viewCustomer'),
    path('ntnbms/search', views.search, name='search'),
    path('ntnbms/searchCustomer', views.searchCustomer, name='searchCustomer'),
    path('ntnbms/view/<key>/', views.view, name='view'), 
    path('ntnbms/edit_record/<key>/', views.edit_record, name='edit_record'),
    path('ntnbms/edit_customer_record/<key>/', views.edit_customer_record, name='edit_customer_record'),
    path('ntnbms/update_record/<key>/', views.update_record, name='update_record'),
    path('ntnbms/update_customer_record/<key>/', views.update_customer_record, name='update_customer_record'), 
    path('ntnbms/new', views.new, name='new'),
    path('ntnbms/newCustomer', views.newCustomer, name='newCustomer'),

]