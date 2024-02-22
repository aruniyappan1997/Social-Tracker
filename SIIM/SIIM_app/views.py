from django.shortcuts import render
from django.template import loader

# Create your views here.
def Home(request):
    return render(request,"Home.html")

def Login(request):
    return render(request, "Login.html")

def Logout(request):
    return render(request, "Logout.html")
    