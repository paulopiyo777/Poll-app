# URL configuration through which views are mapped
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
