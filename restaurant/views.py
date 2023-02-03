from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum
from django.contrib import messages



def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    
def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'book.html', {'bookings': bookings})

from datetime import datetime

@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        no_of_guest = request.POST.get('no_of_guest')
        booking_date_str = request.POST.get('bookingDate')

        # Convert the string representation of the date to a datetime object
        booking_date = datetime.strptime(booking_date_str, '%Y-%m-%dT%H:%M')
        
        hour_bookings = Booking.objects.filter(bookingDate__year=booking_date.year,
                                               bookingDate__month=booking_date.month,
                                               bookingDate__day=booking_date.day,
                                               bookingDate__hour=booking_date.hour).aggregate(total=Sum('no_of_guest'))
        hour_total = hour_bookings['total'] or 0
        if hour_total + int(no_of_guest) > 20:
            messages.info(request, 'Number of slots exceeded, kindly choose another time')
        else:
            Booking.objects.create(
                name=name,
                email=email,
                no_of_guest=no_of_guest,
                bookingDate=booking_date
            )
            messages.info(request,'Booking was successful')

        return redirect('book')

    bookings = Booking.objects.all()
    hour_bookings = Booking.objects.all().values('bookingDate').annotate(total=Sum('no_of_guest'))
    hour_slots = {}
    for hour_booking in hour_bookings:
        hour = hour_booking['bookingDate'].strftime("%Y-%m-%d %H:00")
        if hour_booking['total'] <= 20:
            slots = 20 - hour_booking['total']
            hour_slots[hour] = slots
            
    slots_left = sorted(hour_slots.items())
    context = {
        'hour_slots' : hour_slots,
        'bookings': bookings,
        'slots_left': slots_left,
    }
    return render(request, 'book.html', context)



        
class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    
    
    
def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})




def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 