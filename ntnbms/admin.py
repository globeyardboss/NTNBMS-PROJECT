from django.contrib import admin
from .models import customer
from .models import booking

admin.site.register(customer)
admin.site.register(booking)


admin.site.site_title = "<NTNBMS>"
admin.site.site_header = "NTN Booking and Management System Admin Page"
admin.site.index_title = "Site Administration"
