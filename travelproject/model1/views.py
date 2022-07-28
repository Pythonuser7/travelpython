from django.shortcuts import render
from django.shortcuts import render
from. models import Place
from. models import Panelmembers
def demo3(request):
    obj = Place.objects.all()
    obj2 = Panelmembers.objects.all()
    return render(request, "index.html", {'result': obj, 'result2': obj2})
# Create your views here.
