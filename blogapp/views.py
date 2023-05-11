from django.shortcuts import render,get_list_or_404
from .models import Blog




def index(request):
    context={
        "blog":Blog.objects.all()
    }
    return render(request,'index.html',context)


def aboutus(request):
    return render(request,'about-us.html')

def condactus(request):
    return render(request,'contact.html')
# Create your views here.

def login(request):
    return render(request,"")


def details(request,id):
    obj=Blog.objects.get(pk=id)
    return render(request,'single-post.html',{"obj":obj})