from django.shortcuts import render
from django.template import loader

# Create your views here.
def Home(request):
    return render(request,"Login.html")
    