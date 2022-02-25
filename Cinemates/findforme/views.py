from django.shortcuts import render

# Create your views here.
def findforme(request):
    return render(request,"findforme/home.html")