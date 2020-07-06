from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'title': 'My blog homepage',
		'welcome': 'Welcome to the homepage of my blog'
	}
	return render(request, 'blog/index.html', context)