from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.


class customer(models.Model):
    CID = models.IntegerField(primary_key=True, null=False)
    First_Name = models.CharField(max_length=25)   
    Last_Name = models.CharField(max_length=25)
    Email = models.EmailField(max_length=50, null=True, blank=True)
    Main_Telephone_Number = models.CharField(max_length=25)
    Other_Telephone_Number = models.CharField(max_length=25, blank=True)



    def __str__(self):
        return self.Last_Name





class booking(models.Model):
    BID = models.IntegerField(primary_key=True, null=False)
    CID = models.ForeignKey('customer', on_delete=models.CASCADE)
    Recipient_Name = models.CharField(max_length=25) 
    Air_Time = models.DateTimeField(blank=True, null=True)
    Number_Of_Showing = models.IntegerField()
    Text_Content = models.TextField(blank=True)
    Image_File = models.ImageField(default='default.png', blank=True)
    Video_File = models.FileField(upload_to='uploads/', null=True, blank=True)
    Air_Date = models.DateField(null=True, blank=True)
    Date_Created = models.DateField(null=True, blank=True)
    

    def __str__(self):
        return self.Recipient_Name
