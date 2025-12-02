from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import RegisterForm, LoginForm


def register_view(request):
    # Если юзер уже авторизован – отправляем на главную
    if request.user.is_authenticated:
        return redirect('homepage:home')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # создаём пользователя
            login(request, user)  # сразу логиним
            messages.success(request, 'Вы успешно зарегистрировались и вошли в аккаунт.')
            return redirect('homepage:home')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = RegisterForm()

    # ВАЖНО: используем существующий шаблон в папке registration
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    # Если юзер уже авторизован – отправляем на главную
    if request.user.is_authenticated:
        return redirect('homepage:home')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно вошли в аккаунт.')
            return redirect('homepage:home')
        else:
            messages.error(request, 'Неверный логин или пароль.')
    else:
        form = LoginForm(request)

    # ВАЖНО: используем существующий шаблон в папке registration
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'Вы вышли из аккаунта.')
    return redirect('homepage:home')
