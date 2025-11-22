from django.urls import path
from . import views

app_name = 'sale'

urlpatterns = [
    path('', views.sale, name='sale'),
    path('seasonal_storage/', views.seasonal_storage, name='seasonal_storage'),
    path('free_tire_service/', views.free_tire_service, name='free_tire_service'),
    path('free_shipping/', views.free_shippping, name='free_shipping'),
    path('sale_doship/', views.sale_doship, name='sale_doship'),
]