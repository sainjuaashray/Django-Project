from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Hobby
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView


# Create your views here.
"""
posts = [
    {
        'name': 'Kise Ryota',
        'hobby': 'Basketball',
        'age': 21
    },
    {
        'name': 'Sakamichi',
        'hobby': 'Cycling',
        'age': 15
    }
]"""


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    #add context when you want to access posts like , context
    return render(request, 'DEMOAPP/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = "DEMOAPP/home.html"#<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post


def about(request):
    return render(request, 'DEMOAPP/about.html', {'title': 'About'})

@login_required
def upload(request):
    return render (request, 'DEMOAPP/upload.html')
