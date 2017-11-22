from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from movie.models import User
from django.contrib.auth import logout, login
from django.contrib.auth import authenticate
import MySQLdb


db = MySQLdb.connect(host="140.119.19.73",user="admin", passwd="12345678", db="bookingmovie")
cursor = db.cursor()
# cursor.execute("SELECT is_staff from movie_user where id = %s ",(id))
# check_staff = cursor.fetchone()


# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        try:
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

        except:
            print('Got exception on main handler')
            raise Http404("Something goes wrong")

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
