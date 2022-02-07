from django.shortcuts import render
from . import function

def index(request):
    films = function.listfilmIMBD("indianajones")
    test = "hello world"
    return render(request,"home/home.html", {"films": films} )

