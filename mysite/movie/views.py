# -*- coding: utf-8 -*-

import json
import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from movie.models import User
from django.contrib.auth import logout, login
from django.contrib.auth import authenticate
import MySQLdb

from movie.models import Movie, Showtimes, Meal, Seat, Order, Combo, OrderMeal, SeatsOrder

db = MySQLdb.connect(host="140.119.19.73",    user="admin", passwd="12345678", db="orm_booking_movie")
cursor = db.cursor()

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
    movies = Movie.objects.all()
    # Redirect to a success page.
    return render(request, 'index.html',{'movies':movies})

def movieDetail(request):
    if request.POST:
        movie_id = request.POST['movie_id']
    
    movie = Movie.objects.get(id=movie_id)
    # cursor.execute("SELECT * FROM showtimes WHERE movie_id = %s",(movie_id))
    # rc = cursor.rowcount
    # row=[]
    #
    # for i in range(0,rc):
    #     rows = cursor.fetchone()
    #     info = "Cinema:" + rows[1] +"  Showtime:"+str(rows[2])+"  Price:"+str(rows[3])
    #     row.append([rows[0],info])
    #
    # print(row)
    row=[]
    showtimes = Showtimes.objects.filter(movie=movie)
    for showtime in showtimes:
        info = "Cinema:" + showtime.cinema +"  Showtime:"+str(showtime.showtime)+"  Price:"+str(showtime.price)
        row.append([showtime.id, info])

    print(row)

    return render(request,'moviedetail.html' , {'movie': movie,'showtime':row} )

def member(request):
    orders = Order.objects.filter(user=request.user)
    ordersList = []
    for order in orders:
        orderTmp = {
            'movie_name': order.showtimes.movie.name,
            'showtime': datetime.datetime.strftime(order.showtimes.showtime, '%Y-%m-%dT%H:%M:%S'),
            'seat': [seatOrder.seat.number for seatOrder in SeatsOrder.objects.filter(order=order)],
            'addition': [orderMeal.meal.name for orderMeal in OrderMeal.objects.filter(order=order)],
            'status': 'Not confirmed',
        }
        ordersList.append(orderTmp)

    context = {
        'orders': ordersList,
    }
    return render(request,'member.html', context)

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
        showtimes_id = request.POST['showtimes']
        combo_id = request.POST.get('combo', None)

        seats = request.POST.getlist('seats')
        meals = request.POST.getlist('meal')

        showtime = Showtimes.objects.filter(id=showtimes_id)[0]

        if combo_id:
            combo = Combo.objects.filter(id=combo_id)[0]
        else:
            combo = None

        order = Order(
            combo=combo,
            showtimes=showtime,
            user=request.user,
            status=1
        )
        order.save()

        for seat_id in seats:
            seat = Seat.objects.filter(id=seat_id)[0]
            seats_order = SeatsOrder(
                seat=seat,
                order=order
            )
            seats_order.save()

        for meal_id in meals:
            meal = Meal.objects.filter(id=meal_id)[0]
            meal_order = OrderMeal(
                meal=meal,
                order=order
            )
            meal_order.save()
        movies = Movie.objects.all()
        meals = Meal.objects.all()

        context = {
            'movies': movies,
            'meals': meals,
        }
        return render(request, 'index.html',context)

def getShowTimes(request):

    movieId = request.GET['movie_id']
    showtimes = Showtimes.objects.filter(movie_id=movieId)

    div = ""

    for showtime in showtimes:
        s = """
            <div class="col-md-12">
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

def addShowTimes(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    if request.POST:
        cinema = request.POST['cinema']
        showtime = request.POST['showtime']
        price = request.POST['price']
        movie_id = request.POST['movie_id']

        showtimes = Showtimes(
            cinema = cinema,
            showtime = showtime,
            price = price,
            movie_id = movie_id
        )
        showtimes.save()
    return render(request,'manager.html',context)

def addMeal(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    if request.POST:
        name = request.POST['name']
        kind = request.POST['kind']
        flavor = request.POST['flavor']
        price = request.POST['price']

        meal = Meal(
            name = name,
            kind = kind,
            flavor = flavor,
            price = price
        )
        meal.save()
    return render(request,'manager.html',context)


def deleteMovie(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    if request.POST:
        id = request.POST['movie_id']
        cursor.execute("DELETE FROM movie WHERE id = %s" %(id))
        db.commit()

    return render(request,'manager.html',context)

def deleteShowtime(request):

    if request.POST:
        sid = request.POST['showtime_id']
        cursor.execute("DELETE FROM showtimes WHERE id = %s" % (sid))
        db.commit()

    movie_id = request.POST['movie_id']
    movie = Movie.objects.get(id=movie_id)
    cursor.execute("SELECT * FROM showtimes WHERE movie_id = %s",(movie_id))
    rc = cursor.rowcount
    row=[]
    for i in range(0,rc):
        rows = cursor.fetchone()
        info = "Cinema:" + rows[1] +"  Showtime:"+str(rows[2])+"  Price:"+str(rows[3])
        row.append([rows[0],info])

    return render(request,'moviedetail.html',{'movie':movie,'showtime':row})
