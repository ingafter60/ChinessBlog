from django.shortcuts import render, get_object_or_404

from .models import Post


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    context = {
    	'post_list': post_list
    }
    return render(request, 'blog/index.html', context)
    # return render(request, 'base.html', context)


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
    	'post': post
    }
    return render(request, 'blog/detail.html', context)    