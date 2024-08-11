from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
# Create your views here.
#views for rendering page
def index(request):
    return render(request, 'index.html')
def book(request):
    return render(request, 'book.html')
def about(request):
    return render(request, 'about.html')
def menu(request):
    return render(request, 'menu.html')
def FrenchFries(request):
    return render(request, 'FrenchFries.html')


#CRUD Operations for Posting food Reviews
