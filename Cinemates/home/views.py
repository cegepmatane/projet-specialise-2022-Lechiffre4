from django.http import HttpResponse
from django.shortcuts import render,redirect
from matplotlib.font_manager import json_dump
from . import function
from .form import Searchform
import FireBaseBDD

def index(request):
    films = []
    return render(request,"home/home.html",{"films": films})

def search(request):
    if request.method == 'POST':
        usersearch_retreived = request.POST.get('search', "")
        Searchform(usersearch_retreived)

        #search in the bdd first
        research_output = FireBaseBDD.searchResearch(usersearch_retreived)


        if(research_output == None):
            films = function.getlistfilmIMBD(usersearch_retreived)  
            films = function.sortFilmOutput(usersearch_retreived, films)

            films_links = []
            films_pics = []
            for i in films:
                film_id = function.getfilmID(i)
                film_pic = function.getPic(film_id)
                films_links.append(film_id)
                films_pics.append(film_pic)

            FireBaseBDD.addResearch(usersearch_retreived, films,films_links,films_pics)

        else:
            films = research_output[0]
            films_links = research_output[1]
            films_pics = research_output[2]

        zippedlist = zip(films, films_links,films_pics)

        page = render(request, "home/Listfilm_model.html", {"films": zippedlist})
       
       
    return page



    





