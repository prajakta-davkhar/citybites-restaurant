from django.shortcuts import render, redirect
from django.contrib import messages
from application.models import *
# Create your views here.


def home(request):
    
    return render(request,'index.html')

def aboutus(request):
    return render(request, 'about.html')

def event(request):
    return render(request, 'event.html')

def menu(request):
    return render(request, 'menu.html')

from django.shortcuts import render, redirect
from .models import Booking

def table(request):
    if request.method == 'POST':
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('phone')
        d = request.POST.get('date')
        e = request.POST.get('time')
        f = request.POST.get('people')
        g = request.POST.get('message')

        # Extract only the date portion (YYYY-MM-DD)
        date_only = d.split(' ')[0] if d and ' ' in d else d  

        # ✅ Save booking data to MySQL
        Booking.objects.create(
            name=a,
            email=b,
            phone=c,
            date=date_only,
            time=e,
            people=f,
            message=g
        )

        # ✅ Redirect after saving
        messages.success(request, "Your table has been booked successfully!")
        return redirect('table')  

    # ✅ Display all bookings
    data = Booking.objects.all()
    return render(request, "table.html", {"data": data})



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # ✅ Automatically save to MySQL table application_enquiry
        Enquiry.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        # ✅ Display success message
        messages.success(request, 'Your enquiry has been sent successfully!')
        return redirect('contact')  # refresh page

    # ✅ Fetch all enquiries from MySQL to show on the page
    all_enquiries = Enquiry.objects.all().order_by('-id')

    return render(request, 'contact.html', {'enquiries': all_enquiries})
