from django.shortcuts import render, redirect
from .models import Profile, Post
from .forms import UserRegistrerForm


def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'twitter/newsfeed.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegistrerForm()
    context = {'form': form}
    return render(request, 'twitter/register.html', context)


def profile(request):

    return render(request, 'twitter/profile.html')


def editar(request):
    return render(request, 'twitter/editar.html')
