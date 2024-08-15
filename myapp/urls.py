from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    path('menu', views.menu, name="menu"),
    path('about', views.about, name="about"),
    path('book', views.book, name="book"),
    path('FrenchFries', views.FrenchFries, name="FrenchFries"),
    path('postlist', views.post_list, name="post_list"),
    path('createpost', views.post_create, name="post_create"),
    path('<int:post_id>/editpost', views.post_edit, name='post_edit'),
    path('<int:post_id>/deletepost', views.post_delete, name='post_delete'),
    path('register/', views.register, name='register'),
]
