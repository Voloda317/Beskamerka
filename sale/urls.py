from django.urls import path
from . import views

app_name = 'sale'

urlpatterns = [
    path('', views.sale_tire_list, name='sale'),
]