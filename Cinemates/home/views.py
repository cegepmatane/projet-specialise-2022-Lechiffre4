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
    return 

def displayfilms(request,user_input):
    films = function.listfilmIMBD(user_input)
    return render(request,"home/home.html",{"films": films})


    





