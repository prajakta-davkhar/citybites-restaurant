from django.contrib import admin

from application.models import *
from .models import Enquiry, Booking


# Register your models here.

admin.site.register(Enquiry)
admin.site.register(Booking)