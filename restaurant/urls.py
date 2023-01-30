from django.urls import path
from . import views
from .views import MenuView
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', MenuView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
    
    # path('booking/', BookingView.as_view()),
    
    
]