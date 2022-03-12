from django.http import HttpResponse
from django.shortcuts import render,redirect
from matplotlib.font_manager import json_dump
from . import functions
from .form import FormFindForMe

# Create your views here.
def findforme(request):
    films = []
    return render(request,"findforme/home.html",{"films": films})

def search(request):
    if request.method == 'POST':
        user_category = request.POST.get('category', "")
        FormFindForMe(user_category)

        result = None
        
        while result is None:
            try:
                films_title = functions.getRandomFilm(user_category)
                films_link = []
                for film in films_title:
                    films_link.append(functions.getfilmID(film))
                result = 0
            except:
                pass


        zippedlist = zip(films_title, films_link)
        page = render(request, "findforme/ListRandomFilm.html",{"films": zippedlist})
       
    return page