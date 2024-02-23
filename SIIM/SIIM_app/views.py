from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def Home(request):
    return render(request,"Home.html")

def Login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print("username and password are wrong")
        if username != "arun":
            messages.info(request,"Username is incorrect")
        elif password != "123":
            messages.info(request,"Password in Wrong")
        elif username == "arun" and password == "123":
            messages.info(request,"Logged in Successfully")
            return render(request, 'Home.html')
        return redirect("Login")
    return render(request, "Login.html")

def Logout(request):
    messages.success(request,"Logged out successfully")
    return redirect('Login')
    