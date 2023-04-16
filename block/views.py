from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("this is my first url")
def specific(request):
    return HttpResponse("this is the specific url")


def article(request,article_id):
    return render(request,'block/index.html',{'article_id':article_id})