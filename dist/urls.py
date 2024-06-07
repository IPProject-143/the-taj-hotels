from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_page, name = "homepage"),
    path("hotels", views.hotels, name = "hotels"),
    path("aboutus", views.aboutus, name = "aboutus"),
    path("login", views.loginpage, name = "login"),
    path("services", views.services, name = "services"),
    path("get-in-touch", views.getintouch, name = "get"),
    path("register", views.registerpage, name = "register"),
    path("logout", views.logoutpage, name = "logout"),
    path("dashboard", views.dashboard, name = "dashboard"),
    path('book/<str:place>/', views.booking, name = "booking"),
]