from django.http import HttpResponse
from django.shortcuts import render
from mysql.models import *


# Create your views here.
def index(request):
    return HttpResponse("Welcome to Mysql!")


def mysql_index(request):
    mysql_list = OrderNew.objects.all()  # 获取所有数据
    return render(request,'mysql_index.html', {'mysql_list':mysql_list})   # 返回index.html页面
