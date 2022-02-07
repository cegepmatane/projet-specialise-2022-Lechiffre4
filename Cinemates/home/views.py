from django.http import HttpResponse
from django.shortcuts import render
from . import function
from .form import Searchform

def index(request):
    films = []
    return render(request,"home/home.html",{"films": films})

def search(request):
    if request.method == 'POST':
       usersearch_retreived = request.POST.get('search')

       Searchform(usersearch_retreived)
    films = function.listfilmIMBD(usersearch_retreived)
    print(films)
    return render(request,"home/home.html", {"films": films} )



