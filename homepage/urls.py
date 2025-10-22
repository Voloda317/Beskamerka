from django.urls import path
from . import views

app_name = 'homepage'  # Добавьте эту строку

urlpatterns = [
    path('', views.home, name='home'),

]