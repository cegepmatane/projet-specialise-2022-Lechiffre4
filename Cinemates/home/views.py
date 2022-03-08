from django.http import HttpResponse
from django.shortcuts import render,redirect
from matplotlib.font_manager import json_dump
from . import function
from .form import Searchform

def index(request):
    films = []
    return render(request,"home/home.html",{"films": films})

def search(request):
    if request.method == 'POST':
       usersearch_retreived = request.POST.get('search', "")
       Searchform(usersearch_retreived)
       films = function.getlistfilmIMBD(usersearch_retreived)  
       films = function.sortFilmOutput(usersearch_retreived, films)
       
       films_links = []
       for i in films:
           film_id = function.getfilmID(i)
           films_links.append(film_id)
        
       zippedlist = zip(films, films_links)

       page = render(request, "home/Listfilm_model.html", {"films": zippedlist})
       
    return page



    





