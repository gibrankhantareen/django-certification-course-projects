from django.urls import path

from . import views

urlpatterns = [
    path('', views.homPageView, name='Home'),
]
