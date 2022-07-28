from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo1(request):
    name = "India"
    return render(request, "index2.html", {'obj':name})
def addition(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    res=x+y
    return render(request, "result.html", {'result':res})
# Create your views here.

# Create your views here.
