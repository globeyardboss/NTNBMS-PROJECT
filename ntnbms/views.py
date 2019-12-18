from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def login(request):
    return render(request, 'ntnbms/login.html', {})


def home(request):
    return render(request, 'ntnbms/home.html', {})