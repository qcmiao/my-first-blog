from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Post
from django.utils import timezone

# Create your views here.
def homePage(request):
    return HttpResponse("<h1>This is home page<h1>")
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts': posts})
