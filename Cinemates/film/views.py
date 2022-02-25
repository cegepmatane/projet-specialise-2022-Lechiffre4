from django.shortcuts import render

# Create your views here.
def film(request):
    return render(request,"film/home.html")