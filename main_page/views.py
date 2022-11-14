from django.shortcuts import render
from django.http import HttpResponse


def greeting_view(request):
    return render(request, 'main_page/greeting.html')

def biography_view(request):
    return render(request, 'main_page/biography.html')
