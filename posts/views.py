from django.shortcuts import render
from .models import Post

def index(request):
    post_model = Post.objects.all()
    return render(request, 'index.html', {"posts": post_model})
