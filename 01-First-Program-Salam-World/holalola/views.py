from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def NayaHomePageView(request):
    return HttpResponse('Assalamualaikum means May Peace be upon you. This is my first Django App. Made by Gibran Khan Tareen')