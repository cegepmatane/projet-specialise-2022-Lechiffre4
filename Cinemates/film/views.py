from django.shortcuts import render
from django.http import HttpResponse
from . import function

# Create your views here.
def film(request):
    return render(request,"film/home.html")

def film_id(request,id):
    film_infos = function.GetInfo(id)
    print(film_infos)
    return render(request,"film/home.html",film_infos)
