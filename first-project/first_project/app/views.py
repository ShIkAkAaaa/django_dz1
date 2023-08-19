import os

from django.http import HttpResponse
from django.shortcuts import render, reverse

import datetime

def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    return HttpResponse(f'Текущее время: {datetime.datetime.now().time()}')


def workdir_view(request):
    files = os.listdir(os.getcwd())
    msg = f'{files}'
    return HttpResponse(msg)
