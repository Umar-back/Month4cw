from django.shortcuts import HttpResponse, render

from post.models import Post
# CBV - Class Based View
# FBV - Function Based View
# PEP8 - Python
# snake_case, CamelCase

def main_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()  # QuerySet

        return render(request,'index.html')

def posts_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()

        context = {
            "posts": posts,
        }

        return render(request,'posts/posts.html', context=context)

