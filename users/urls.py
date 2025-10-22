from django.urls import path
from . import views

app_name = 'users'  # Добавьте эту строку

urlpatterns = [
    path('', views.users, name='users'),  # Пример пути
]