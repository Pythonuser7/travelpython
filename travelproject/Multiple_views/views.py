from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demo1(request):
    return render(request,"intex.html")
def about(request):
    return render(request,"about.html")
