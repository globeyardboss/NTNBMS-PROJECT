from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='login'),
    path('ntnbms/home', views.home, name='home'),
]