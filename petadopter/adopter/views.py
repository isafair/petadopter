from django.shortcuts import render, redirect
from django.views import generic
from .models import Post
from . import forms
from django.contrib.auth.decorators import login_required


# Create your views here.


def PostList(request):
    posts = Post.objects.all().order_by('updated_on')
    # return render(request,'recipes/recipe_list.html',{'recipes':recipes})
    return render(request, 'adopter/post_list.html', {'posts': posts})


def PostDetail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'adopter/post_detail.html', {'post': post})


def PostCreate(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        # create a form instance and populate it with data from the request:
        if form.is_valid():
            # process data and return to exercise list
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('adopter:list')
    else:
        form = forms.CreatePost()
        return render(request, 'adopter/post_create.html', {'form': form})
