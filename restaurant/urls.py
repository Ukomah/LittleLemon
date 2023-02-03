from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserRegistrationView



urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.bookings, name='book'),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    path('api-token-auth/', obtain_auth_token),
    
    # path('booking/', BookingView.as_view()),
    
    
]