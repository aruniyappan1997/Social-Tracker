from django.shortcuts import render, redirect

# Create your views here.
def Home(request):
    return render(request,"Home.html")

def Login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print("username and password are wrong")
        if username == "arun" and password == "123":
            return redirect('Home')
        return redirect("Login")
    return render(request, "Login.html")

def Logout(request):
    return redirect('Login')
    