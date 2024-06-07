from django.shortcuts import render, redirect 
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ucform, dates
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CouplesRoom, VIPRooms, NormalRoom, hotel

# Create your views here.
def home_page(request):
    return render(request, "index.html")

@login_required(login_url = "login")
def hotels(request):
    
    return render(request, "hotels.html")


def aboutus(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def getintouch(request):
    if request.method == "POST":

        message = f"""
            <h1>This is a new submission made by {request.POST.get("username")} in your get-in-touch form</h1>

            <p>{request.POST.get("message")}</p>
        """

        send_mail(f"New submission in get-in-touch from {request.POST.get('username')}", 
                   from_email = request.POST.get("email"),
                   message = message,
                   recipient_list = ["ipprojectnoreply@gmail.com"], 
                   fail_silently = False,
                   html_message = message)       
        
    
    return render(request, "getintouch.html")

def registerpage(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    else:
        form = ucform()
        
        if request.method == "POST":
            form = ucform(request.POST)
            
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get("username")
                messages.success(request, "Account was created for " + user + "!")
                return redirect("login")

        return render(request, "register.html", {
            "form": form
        })

def loginpage(request):

    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
        if request.method == "POST":
            name = request.POST.get("username")
            passw = request.POST.get("password")

            user = authenticate(request, username = name, password = passw)

            if user is not None:
                login(request, user)
                redirect("/")
            else:
                messages.info(request, "Username or password is incorrect")
                
        return render(request, "login.html")


def logoutpage(request):
    logout(request)
    return redirect("login")

@login_required(login_url = "login")
def dashboard(request):

    try:
        normal = NormalRoom.objects.filter(user = request.user)
        vip = VIPRooms.objects.filter(user = request.user)
        couples = CouplesRoom.objects.filter(user = request.user)

    except Exception as e:
        print(e)
    return render(request, "user-dashboard.html", {
        "normal": normal,
        "vip": vip,
        "couples": couples
    })

@login_required(login_url = "login")
def booking(request, place):
    date = dates()
    
    hoteles = {
        "Bangkok": 0,
        "Cape Town": 1,
        "Chennai": 2,
        "New Delhi": 3,
        "Dubai": 4,
        "France": 5,
        "Istanbul": 6,
        "Tokyo": 7,
        "Kuala Lumpur": 8,
        "London": 9,
        "Mumbai": 10,
        "New York": 11,
        "Rio De Janeiro": 12,
        "Rome": 13,
        "Sydney": 14,
    }

    if request.method == "POST":
        pl = request.POST.get("location")
        checkin = request.POST.get("checkin")
        checkout = request.POST.get("checkout")
        room = request.POST.get("room")
        adult = request.POST.get("adults")
        kids = request.POST.get("kids")
        service = request.POST.get("services")

        if service == "on":
            service = True
        else:
            service = False

        if room == "normal":
            nrom = NormalRoom(start_date = checkin, end_date = checkout, no_of_adults = adult, no_of_kids = kids, booked = True, vip_services = service, hotel_location = hotel.objects.all()[hoteles[pl]], user = request.user)
            nrom.save() 
            redirect("dashboard")
        
        elif room == "vip":
            vrom = VIPRooms(start_date = checkin, end_date = checkout, no_of_adults = adult, no_of_kids = kids, booked = True, vip_services = service, hotel_location = hotel.objects.all()[hoteles[pl]], user = request.user)
            vrom.save()
            redirect("dashboard")
        
        elif room == "couples":
            crom = CouplesRoom(start_date = checkin, end_date = checkout, no_of_adults = adult, no_of_kids = kids, booked = True, vip_services = service, hotel_location = hotel.objects.all()[hoteles[pl]], user = request.user)
            crom.save()
            redirect("dashboard")

    return render(request, "booking.html", {"place": place, "form": date})