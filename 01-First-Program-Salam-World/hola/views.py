from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def homPageView(request):
    return HttpResponse('Hola is Hello in Spanis')