from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo1(request):
    name = "India"
    return render(request, "intex.html",{'obj':name})

# Create your views here.
