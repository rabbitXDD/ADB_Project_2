"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import Iuno

from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView

from movie.views import register
from movie.views import index
from movie.views import member
from movie.views import manager
from movie.views import logoutUser, signin
from movie.views import booking
from movie.views import getShowTimes
from movie.views import getSeats
from movie.views import addShowTimes
from movie.views import addMeal
from movie.views import movieDetail
from movie.views import deleteMovie
from movie.views import deleteShowtime
from movie.views import changeConfirm
from movie.views import getOrder
from movie.views import editOrderStatus
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

]

# put this before django-cms urls,
# see https://stackoverflow.com/questions/22705939/
# django-debug-toolbar-shows-up-but-the-panels-return-404
if settings.DEBUG:
    Iuno.attachDebugURLs(settings, urlpatterns)

urlpatterns += patterns('',
        url(r'^member',member,name="member"),
        url(r'^manager',manager,name="manager"),
        url(r'^register',register, name="register"),
        url(r'^logout', logoutUser, name="logout"),
        url(r'^login', signin, name="signin"),
        url(r'^booking', booking, name="booking"),
        url(r'^showtimes', getShowTimes, name="getShowTimes"),
        url(r'^showseats', getSeats, name="getSeats"),
        url(r'^addShowTime', addShowTimes, name = "addShowTimes"),
        url(r'^addMeal', addMeal, name = "addMeal"),
        url(r'^movieDetail', movieDetail, name = "movieDetail"),
        url(r'^deleteMovie',deleteMovie,name="deleteMovie"),
        url(r'^deleteShowtime',deleteShowtime,name="deleteShowtime"),
        url(r'^changeConfirm',changeConfirm,name="changeConfirm"),
        url(r'^getorder',getOrder,name="getOrder"),
        url(r'^editorderstatus', editOrderStatus, name="editOrderStatus"),
        url(r'', index),
)
