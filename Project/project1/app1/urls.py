from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index),
    path("name/", views.index2),
    path("hello/",views.httpTemp)
]
