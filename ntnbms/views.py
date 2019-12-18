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



def view(request, key):
    detail = personal_information.objects.get(InternID=key)
    result = internship_history.objects.filter(InternID=key)
    query_set = qualifications_on_entry.objects.filter(InternID=key)
    return render(request, 'database/view.html', {'personal_information': detail, 'internship_history': result, 'qualifications_on_entry': query_set})
