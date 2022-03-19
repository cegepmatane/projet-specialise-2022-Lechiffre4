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
       films_pics = []
       for i in films:
           film_id = function.getfilmID(i)
           film_pic = function.getPic(film_id)
           films_links.append(film_id)
           films_pics.append(film_pic)
           
        
       zippedlist = zip(films, films_links,films_pics)

       page = render(request, "home/Listfilm_model.html", {"films": zippedlist})
       
    return page



    





