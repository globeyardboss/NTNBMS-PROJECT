from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import booking
from .models import customer


# Create your views here.
def login(request):
    return render(request, 'ntnbms/login.html', {})


def home(request):
    Booking = booking.objects.all()
    Booking = booking.objects.order_by('BID')
    return render(request, 'ntnbms/home.html', {'Booking': Booking})


def viewCustomer(request):
    Customer = customer.objects.all()
    Customer = customer.objects.order_by('CID')
    return render(request, 'ntnbms/viewCustomer.html', {'Customer': Customer})
    
    


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




@csrf_exempt
def newCustomer(request):
   
    if request.method == 'POST':
        newCustomer=customer()
        newCustomer.CID = request.POST.get('CustomerID')
        newCustomer.First_Name = request.POST.get('FirstName')
        newCustomer.Last_Name = request.POST.get('LastName')
        newCustomer.Email = request.POST.get('Email')
        newCustomer.Main_Telephone_Number = request.POST.get('Main_Telephone')
        newCustomer.Other_Telephone_Number = request.POST.get('Other_Telephone')
        newCustomer.save()

        context = {
            'BookinID': newCustomer.CID,
            'CustomerID': newCustomer.First_Name,
            'Recepient_Name': newCustomer.Last_Name,
            'Email': newCustomer.Email,
            'Main_Telephone': newCustomer.Main_Telephone_Number,
            'Other_Telephone': newCustomer.Other_Telephone_Number,
            
        }
        

        return render(request, 'ntnbms/new.html', {})
    
    else:
        return render(request, 'ntnbms/new.html', {})



def view(request, key):
    detail = booking.objects.get(BID=key)
    return render(request, 'ntnbms/view.html', {'booking': detail})





def edit_record(request, key): 
    detail = booking.objects.get(BID=key)
    return render(request, 'ntnbms/edit.html', {'booking': detail})



def edit_customer_record(request, key): 
    detail = customer.objects.get(CID=key)
    return render(request, 'ntnbms/editCustomer.html', {'customer': detail})   




def update_record(request, key):
    det = booking.objects.get(CID=key)
    if request.method == 'POST':
        det.Recepient_Name = request.POST.get('three')  
        det.Number_Of_Showing = request.POST.get('four') 
        det.Air_Time = request.POST.get('five')   
        det.Text_Content = request.POST.get('six')
        det.Air_Date = request.POST.get('seven')
        det.Image_File = request.POST.get('eight')
        det.Video_File = request.POST.get('nine')
        det.Date_Created = request.POST.get('ten')
        det.save()
        return HttpResponseRedirect('/ntnbms/edit_record/%s/' % key)



def update_customer_record(request, key):
    det = customer.objects.get(CID=key)
    if request.method == 'POST':
        det.First_Name = request.POST.get('two')  
        det.Last_Name = request.POST.get('three') 
        det.Email = request.POST.get('four')   
        det.Main_Telephone_Number = request.POST.get('five')
        det.Other_Telephone_Number = request.POST.get('six')
        det.save()
        return HttpResponseRedirect('/ntnbms/edit_customer_record/%s/' % key)
       




def search(request):
    Personal_Information = personal_information.objects.all()
    if request.method == 'POST':
      search_query = request.POST.get('search_item', '')      
      Personal_Information = personal_information.objects.filter(First_Name__icontains= search_query).order_by('InternID') | personal_information.objects.filter(Last_Name__icontains= search_query).order_by('InternID')
      return render(request, 'ntnbms/search.html', {'Personal_Information': Personal_Information})

    else:
         # return render(request, 'ntnbms/home.html', {})
         return HttpResponse('Nothing to display')