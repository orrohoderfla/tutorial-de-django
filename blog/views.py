from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Alfredo Ch',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 5, 2019'
    },
    {
        'author': 'Andres Chorro',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 6, 2019'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
