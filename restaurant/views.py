from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, routers
from rest_framework.response import Response
from .models import Menu,Booking
from .serializers import MenuSerializer, BookingSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# class BookingView(APIView):
    
#     def get(self, request):
#         items = Booking.objects.all()
#         serializer = BookingSerializer(items, many=True)
#         return Response(serializer.data)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
        



class MenuView(APIView):
    
    def get(self, request):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})