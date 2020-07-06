from django.shortcuts import render
from .models import Post


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    context = {
    	'post_list': post_list
    }
    return render(request, 'blog/index.html', context)