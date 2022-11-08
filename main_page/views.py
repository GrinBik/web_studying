from django.shortcuts import render
from django.http import HttpResponse

def greeting_view(request):

	return HttpResponse("Привет! Меня зовут Григорий. Мне 35 лет, женат, детей нет.")