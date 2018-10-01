from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    paramas = {
        'title':'Hello/index',
        'msg':'これはテンプレートを利用しています',
        'goto':'next',
    }
    return render(request, 'hello/index.html',paramas)


def next(request):
    paramas = {
        'title':'Hello/index',
        'msg':'これはテンプレートを利用しています',
        'goto':'index',
    }
    return render(request, 'hello/index.html',paramas)
