from django.contrib import admin
from .models import customer
from .models import booking

admin.site.register(customer)
admin.site.register(booking)


