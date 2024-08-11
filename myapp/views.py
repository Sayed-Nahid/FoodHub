from django.shortcuts import render, get_object_or_404, redirect
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
#Read Operation for Post
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})

#Creat Operation for posting into system
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})

#Update operation code
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id, user = request.user)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'post_form.html', {'form': form})

#Delete Operation for post
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id, user = request.user)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request, 'post_confirm_delete.html', {'post': post})