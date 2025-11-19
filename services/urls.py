from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.services_list, name='services'),
    path('tire-services/', views.tire_services, name='tire_services'),
    path('balancing', views.balancing, name='balancing'), 
    path('pravka', views.pravka, name='pravka'),
    path('remont', views.remont, name='remont'),
    path('keeping-tires/', views.keeping_tires, name='keeping_tires'),
]