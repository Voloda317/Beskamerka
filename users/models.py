from django.db import models

# Create your models here.
from django.db import models

class Users(models.Model):
    user = models.CharField(max_length=20, verbose_name='имя пользователя')
    surname = models.CharField(max_length=20 ,verbose_name='фамилия')
    email = models.EmailField(verbose_name='электронная почта')
    phone = models.CharField(max_length=15, verbose_name='номер телефона')
    password = models.CharField(max_length=20, verbose_name='пароль')

    class Meta:
        verbose_name = 'пользователя'
        verbose_name_plural = 'пользователи'    

    def __str__(self):  
        return self.users