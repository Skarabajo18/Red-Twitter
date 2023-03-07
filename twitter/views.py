from django.shortcuts import render
from .models import Profile, Post


def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'twitter/newsfeed.html', context)


def register(request):
    return render(request, 'twitter/register.html')


def profile(request):

    return render(request, 'twitter/profile.html')


def editar(request):
    return render(request, 'twitter/editar.html')
