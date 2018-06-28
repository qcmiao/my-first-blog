from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def homePage(request):
    return HttpResponse("<h1>This is home page<h1>")
def post_list(request):
    return render(request, 'blog/post_list.html',{})
