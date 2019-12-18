from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views



'''
urlpatterns = [


    url(r'^getdata/', views.new),


]
'''


urlpatterns = [
    path('', views.login, name='login'),
    path('ntnbms/home', views.home, name='home'),
    path('ntnbms/search', views.search, name='search'),
    path('ntnbms/view/<key>/', views.view, name='view'), 
    path('ntnbms/edit_record/<key>/', views.edit_record, name='edit_record'),
    path('ntnbms/update_record/<key>/', views.update_record, name='update_record'),
    path('ntnbms/new', views.new, name='new'),
]