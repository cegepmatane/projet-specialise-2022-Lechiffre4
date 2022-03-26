from django.shortcuts import render
from .form import ContactForm
from . import functions

# Create your views here.
def about(request):
    return render(request,"about/home.html")

def sendMail(request):
    if request.method == 'POST':
        username_retreived = request.POST.get('name', "")
        usersmail_retreived = request.POST.get('mail', "")
        usersmessage_retreived = request.POST.get('message', "")
        ContactForm(username_retreived,usersmail_retreived,usersmessage_retreived)
        functions.SendMail(username_retreived,usersmail_retreived,usersmessage_retreived)
    return render(request,"about/home.html")
        
       
