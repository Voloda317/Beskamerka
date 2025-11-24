from django.urls import path
from . import views

app_name = 'akb'    

urlpatterns = [
    path('', views.AkbListView.as_view(), name='akb'),
    path('<int:pk>/', views.AkbDetailView.as_view(), name='akb_detail'),

]