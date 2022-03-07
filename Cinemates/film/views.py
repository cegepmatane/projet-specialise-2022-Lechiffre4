from django.shortcuts import render
from django.http import HttpResponse
from . import function

# Create your views here.
def film(request):
    return render(request,"film/home.html")

def film_id(request,id):
    Film_name = function.GetInfo(id)
    return render(request,"film/home.html",{"film_name":Film_name})
