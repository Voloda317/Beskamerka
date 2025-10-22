from django.urls import path
from . import views

app_name = 'disks'

urlpatterns = [
    path('', views.DiskListView.as_view(), name='disks'),
]