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



@csrf_exempt
def new(request):
   
    if request.method == 'POST':
        new=personal_information()
        new.First_Name = request.POST.get('First_Name')
        new.Last_Name = request.POST.get('Last_Name')
        new.Other_Name = request.POST.get('Other_Name')
        new.save()

        context = {
            'First_Name': new.First_Name,
            'Last_Name': new.Last_Name,
            'Other_Name': new.Other_Name
        }
        

        return render(request, 'ntnbms/new.html', {})
    

    else:
        return render(request, 'ntnbms/new.html', {})





def view(request, key):
    detail = personal_information.objects.get(InternID=key)
    result = internship_history.objects.filter(InternID=key)
    query_set = qualifications_on_entry.objects.filter(InternID=key)
    return render(request, 'ntnbms/view.html', {'personal_information': detail, 'internship_history': result, 'qualifications_on_entry': query_set})



    def edit_record(request, key): 
    detail = personal_information.objects.get(InternID=key)
    result = internship_history.objects.filter(InternID=key)
    query_set = qualifications_on_entry.objects.filter(InternID=key)
    return render(request, 'ntnbms/edit.html', {'personal_information': detail, 'internship_history': result, 'qualifications_on_entry': query_set})




def search(request):
    Personal_Information = personal_information.objects.all()
    if request.method == 'POST':
      search_query = request.POST.get('search_item', '')      
      Personal_Information = personal_information.objects.filter(First_Name__icontains= search_query).order_by('InternID') | personal_information.objects.filter(Last_Name__icontains= search_query).order_by('InternID')
      return render(request, 'ntnbms/search.html', {'Personal_Information': Personal_Information})

    else:
         # return render(request, 'ntnbms/home.html', {})
         return HttpResponse('Nothing to display')