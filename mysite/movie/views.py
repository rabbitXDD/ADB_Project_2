import json

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from movie.models import User
from django.contrib.auth import logout, login
from django.contrib.auth import authenticate
import MySQLdb

# Create your views here.
def index(request):
    from movie.models import Movie
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'index.html', context)

def register(request):
    if request.method == 'POST':
        # try:
        user = User.objects.create_user(
            username=request.POST['Name'],
            birthday=request.POST['Birthday'],
            email=request.POST['Email'],
            phoneNumber=request.POST['PhoneNumber'],
            password=request.POST['Password']
        )

        user.save()

        user = authenticate(
            username=request.POST['Name'],
            password=request.POST['Password'],
        )

        login(request, user)
        return redirect('/')

        # except:
        #     print('Got exception on main handler')
        #     raise Http404("Something goes wrong")

    else:
        return render(request,'register.html')

def signin(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['Name'],
            password=request.POST['Password'],
        )
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            pass

def logoutUser(request):
    logout(request)
    # Redirect to a success page.
    return render(request, 'index.html')
def member(request):
    return render(request,'member.html')
def manager(request):
    return render(request,'manager.html')

def booking(request):
    if request.POST:
        return render(request, 'index.html')

def getShowTimes(request):
    s = """
        <div class="col-md-1">
            <a href="#select_meals" onclick="showSeats('showseats');$('#showtimes_1').prop('checked', true);" class="scroll btn btn-default"> 
                13:00
            </a>
            <br><input type="checkbox" value="1" id="showtimes_1" name="showtimes">
        </div>
        <div class="col-md-1">
            <a href="#select_meals" onclick="$('#showtimes_1').prop('checked', true);" class="scroll btn btn-default"> 
                13:00
            </a>
            <br><input type="checkbox" value="1" id="showtimes_1" name="showtimes">
        </div>
    """
    return HttpResponse(json.dumps(s.strip('\n')), content_type="application/json")

def getSeats(request):
    s = """
         <div class="col-md-1">
            <a href="#blog" onclick="$('#seats_1').prop('checked', true);" class="scroll btn btn-default"> 
                1
            </a>
            <br><input type="checkbox" value="1" id="seats_1" name="seats">
         </div>
        <div class="col-md-1">
            <a href="#blog" onclick="$('#seats_2').prop('checked', true);" class="scroll btn btn-default"> 
                2
            </a>
            <br><input type="checkbox" value="2" id="seats_2" name="seats">
         </div>
        <div class="col-md-1">
            <a href="#blog" onclick="$('#seats_3').prop('checked', true);" class="scroll btn btn-default"> 
                3
            </a>
            <br><input type="checkbox" value="3" id="seats_3" name="seats">
         </div>
        <div class="col-md-1">
            <a href="#blog" onclick="$('#seats_4').prop('checked', true);" class="scroll btn btn-default"> 
                4
            </a>
            <br><input type="checkbox" value="4" id="seats_4" name="seats">
         </div>
        """
    return HttpResponse(json.dumps(s.strip('\n')), content_type="application/json")

