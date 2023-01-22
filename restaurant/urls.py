from django.urls import path
from . import views
from .views import MenuView



urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', MenuView.as_view()),
    # path('booking/', BookingView.as_view()),
    
    
]