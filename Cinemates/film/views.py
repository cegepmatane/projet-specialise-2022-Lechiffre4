from django.shortcuts import render
from django.http import HttpResponse
from . import function
import FireBaseBDD

# Create your views here.
def film(request):
    return render(request,"film/home.html")

def film_id(request,id):
    film_infos_bdd = FireBaseBDD.searchFilm(id)
    if film_infos_bdd == None:
        film_infos = function.GetInfo(id)
        FireBaseBDD.addFilm(film_infos)
    else : 
        film_infos = film_infos_bdd.val()

    print(film_infos)
    return render(request,"film/home.html",film_infos)
