from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def Home(request):
    template = loader.get_template("Login.html")
    return HttpResponse(template.render())
    