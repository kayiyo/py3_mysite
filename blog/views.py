from django.http import HttpResponse
from django.shortcuts import render
from blog.models import BlogsPost


# Create your views here.
def index(request):
    return HttpResponse("Welcome to QBlog!")


def blog_index(request):
    blog_list = BlogsPost.objects.all()  # 获取所有数据
    return render(request,'index.html', {'blog_list':blog_list})   # 返回index.html页面


def blog_home(request):
    home_list = BlogsPost.objects.all()
    return render(request, 'home.html', {'blog_list': home_list})  # 返回home.html页面


def add(request):
    # a = request.GET['a']
    a = request.GET.get('a',0)
    # b = request.GET['b']
    b = request.GET.get('b', 0)
    c = int(a)+int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add_index(request):
    return render(request, 'add_home.html')