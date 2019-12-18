from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import booking


# Create your views here.
def login(request):
    return render(request, 'ntnbms/login.html', {})


def home(request):
    Booking = booking.objects.all()
    Booking = booking.objects.order_by('BID')
    return render(request, 'ntnbms/home.html', {'Booking': Booking})
    


@csrf_exempt
def new(request):
   
    if request.method == 'POST':
        new=booking()
        new.BID = request.POST.get('BookingID')
        new.CID = request.POST.get('CustomerID')
        new.Recepient_Name = request.POST.get('Recepient_Name')
        new.Number_Of_Showing = request.POST.get('Number_Of_Showing')
        new.Text_Content = request.POST.get('TextContent')
        new.Image_File = request.POST.get('Image')
        new.Video_File = request.POST.get('Video')
        new.Date_Created = request.POST.get('DateCreated')
        new.save()

        context = {
            'BookingID': new.BID,
            'CustoerID': new.CID,
            'Recepient_Name': new.Recepient_Name,
            'Number_Of_Showing': new.Number_Of_Showing,
            'TextContent': new.Text_Content,
            'Image': new.Image_File,
            'Video': new.Vido_File,
            'DateCreated': new.Date_Created
        }
        

        return render(request, 'ntnbms/new.html', {})
    

    else:
        return render(request, 'ntnbms/new.html', {})





def view(request, key):
    detail = booking.objects.get(BID=key)
    return render(request, 'ntnbms/view.html', {'booking': detail})




   # def edit_record(request, key): 
   # detail = personal_information.objects.get(InternID=key)
   # result = internship_history.objects.filter(InternID=key)
   # query_set = qualifications_on_entry.objects.filter(InternID=key)
   # return render(request, 'ntnbms/edit.html', {'personal_information': detail, 'internship_history': result, 'qualifications_on_entry': query_set})




def update_record(request, key):
    det = personal_information.objects.get(InternID=key)
    res = internship_history.objects.filter(InternID=key)
    sett = qualifications_on_entry.objects.filter(InternID=key)
    if request.method == 'POST':
        det.First_Name = request.POST.get('two')  
        det.Last_Name = request.POST.get('four') 
        det.Other_Name = request.POST.get('six')  
        #det.Date_of_Birth = request.POST.get('ten') 
        det.Gender = request.POST.get('eight')
        det.Nationality = request.POST.get('twelve')
        det.Email = request.POST.get('fourteen')
        det.Home_Telephone = request.POST.get('one')
        det.Mobile_Telephone = request.POST.get('three')
        det.Permanent_Address_Line1 = request.POST.get('five')
        det.Permanent_Address_Line2 = request.POST.get('seven')
        det.City = request.POST.get('nine')
        det.Country = request.POST.get('eleven')
        det.Current_Address_Line1 = request.POST.get('thirteen')
        det.Current_Address_Line2 = request.POST.get('fifteen')
        det.Documents = request.POST.get('sixteen')
        det.save()
        return HttpResponseRedirect('/ntnbms/edit_record/%s/' % key)




def search(request):
    Personal_Information = personal_information.objects.all()
    if request.method == 'POST':
      search_query = request.POST.get('search_item', '')      
      Personal_Information = personal_information.objects.filter(First_Name__icontains= search_query).order_by('InternID') | personal_information.objects.filter(Last_Name__icontains= search_query).order_by('InternID')
      return render(request, 'ntnbms/search.html', {'Personal_Information': Personal_Information})

    else:
         # return render(request, 'ntnbms/home.html', {})
         return HttpResponse('Nothing to display')