from django.http import HttpResponse
from django.shortcuts import render
from .models import  Posts

posts = Posts.objects.all()[:10]

contest = {
    'title' : 'Latest Posts',
    'posts' : posts
}

# Create your views here.
def index(request):
    # return  HttpResponse('Hello from posts')
    return render(request,'posts/index.html',contest)

def details(request,id):
    # return  HttpResponse('Hello from posts')
    post = Posts.objects.get(id=id)
    contest = {
        'post' : post
    }
    return render(request,'posts/details.html',contest)

def about(request):
    return render(request,'posts/about.html')