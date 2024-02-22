from django.urls import path
from .views import Home, Login, Logout

urlpatterns = [
    path('', Login, name="login"),
    path('home/', Home, name="home"),
    path('logout/', Logout, name="logut"),
]