from django.shortcuts import render
from .models import Post


def homepage(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'main/homepage.html', context)


def about(request):
    return render(request, 'main/about.html', context={'title': 'About'})


    