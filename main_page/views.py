from django.shortcuts import render
from django.http import HttpResponse


def greeting_view(request):
    answer = 'Привет! Меня зовут Григорий. Мне 35 лет, женат, детей нет.'
    return HttpResponse(answer)
