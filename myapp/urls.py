from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('menu', views.menu, name="menu"),
    path('about', views.about, name="about"),
    path('book', views.book, name="book"),
]
