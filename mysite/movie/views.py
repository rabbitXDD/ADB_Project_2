import json

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from movie.models import User
from django.contrib.auth import logout, login
from django.contrib.auth import authenticate
import MySQLdb

from movie.models import Movie, Showtimes, Meal, Seat

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    meals = Meal.objects.all()

    context = {
        'movies': movies,
        'meals': meals, 
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

    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }

    if request.POST:
        name = request.POST['movie_name']
        type = request.POST['movie_type']
        runtime = request.POST['movie_runtime']
        director = request.POST['movie_director']
        actor = request.POST['movie_actor']
        url = request.POST['movie_imageUrl']

        movie = Movie(
            name=name,
            type=type,
            runtime=runtime,
            director=director,
            actor=actor,
            image=url
        )

        movie.save()

    return render(request,'manager.html', context)

def booking(request):
    if request.POST:
        return render(request, 'index.html')

def getShowTimes(request):
    
    movieId = request.GET['movie_id']
    showtimes = Showtimes.objects.filter(movie_id=movieId)

    div = ""
    
    for showtime in showtimes:
        s = """
            <div class="col-md-2">
                <a href="#select_meals" onclick="showSeats('showseats', %s);$('#showtimes_%s').prop('checked', true);" class="scroll btn btn-default"> 
                    %s
                </a>
                <br><input type="checkbox" value="1" id="showtimes_%s" name="showtimes">
            </div>
        """ % (showtime.id, showtime.id, showtime.showtime.strftime("%Y-%m-%d %H:%M:%S"), showtime.id)
        div += s

    return HttpResponse(json.dumps(div.strip('\n')), content_type="application/json")

def getSeats(request):
    showtimesId = request.GET['showtimes_id']
    seats =  Seat.objects.filter(showtimes_id=showtimesId)
    div = ""

    for seat in seats:
        s = """
            <div class="col-md-1">
                <a href="#blog" onclick="$('#seats_%s').prop('checked', true);" class="scroll btn btn-default"> 
                    %s
                </a>
                <br><input type="checkbox" value="%s" id="seats_%s" name="seats">
            </div>
        """  % (seat.id, seat.number, seat.id, seat.id)

        div += s

    return HttpResponse(json.dumps(div.strip('\n')), content_type="application/json")

