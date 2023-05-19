from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def time_view(request):
    template_name = 'app/time.html'
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    msg = f'Текущее время: {current_time}'
    context = {
        'time': msg
    }
    return render(request, template_name, context)


def workdir_view(request):
    template_name = 'app/direct.html'
    path = '.'
    rez = os.listdir(path)
    context = {
        'workdir': rez
    }
    return render(request, template_name, context)