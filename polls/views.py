from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

#polls主页
def index(request):
    return render(request, 'index.html')

#button按钮
@csrf_exempt
def button(request):
    dic = {'a': 1, 'b': 2, 'c': 3}
    return HttpResponse(json.dumps(dic))

#第一页
def page_one(request):
    return HttpResponse("This is page one")

#第二页
def page_two(request):
    return HttpResponse("122")

