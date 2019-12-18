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