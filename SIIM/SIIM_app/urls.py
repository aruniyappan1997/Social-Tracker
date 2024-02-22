from django.urls import path
from .views import Home, Login, Logout

urlpatterns = [
    path('', Login, name="Login"),
    path('home/', Home, name="Home"),
    path('logout/', Logout, name="Logout"),
]