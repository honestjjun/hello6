from django.shortcuts import render

# Create your views here.
from blog.models import Post


def post(request):
    posts = Post.objects.all()
    return render(request, 'blog/main.jinja', {'posts': posts})
