from django.urls import path
from . import views

app_name = 'tires' 

urlpatterns = [
    path('', views.TireListView.as_view(), name='tires'),
    path('<int:tire_id>/', views.tire_detail, name='tire_detail'), 
]