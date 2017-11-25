from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class User(AbstractUser):
    """
    Custom user class.
    """

    birthday = models.DateField()

    phoneRegex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    phoneNumber = models.CharField(max_length=200, validators=[phoneRegex], blank=True)


# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.

class Meal(models.Model):

    BEVERAGE = 1
    FOOD = 2
    
    MEAL_CHOICES = (
        (BEVERAGE, 'Beverage'),
        (FOOD, 'Food'),
    )

    name = models.CharField(max_length=25)
    kind = models.CharField(
        choices=MEAL_CHOICES,
        default=FOOD,
        max_length=10,
    )
    flavor = models.CharField(max_length=20)
    price = models.CharField(max_length=20)

    class Meta:
        db_table = 'meal'

class Movie(models.Model):
    name = models.CharField(max_length=25)
    type = models.CharField(max_length=20)
    runtime = models.CharField(max_length=20)
    director = models.CharField(max_length=25)
    actor = models.CharField(max_length=50)
    image = models.ImageField()

    class Meta:
        db_table = 'movie'

class Showtimes(models.Model):
    cinema = models.CharField(max_length=10)
    showtime = models.DateTimeField()
    price = models.IntegerField(default=200)
    movie = models.ForeignKey('Movie')
    class Meta:
        db_table = 'showtimes'

class Seat(models.Model):
    showtimes = models.ForeignKey('Showtimes')
    number = models.IntegerField(default=1)

    class Meta:
        db_table = 'seat'

class Combo(models.Model):
    movie = models.ForeignKey('Movie')
    price = models.CharField(max_length=20)

    class Meta:
        db_table = 'combo'

class Combo_Meal(models.Model):
    combo = models.ForeignKey('Combo')
    meal = models.ForeignKey('Meal')

class Order(models.Model):
    
    UNCOMFIRMED = 1
    CONFIRMED = 2
    CANCELED = 3

    ORDER_STATUS_CHOICES = (
        (UNCOMFIRMED, 'Unconfirmed'),
        (CONFIRMED, 'Confirmed'),
        (CANCELED, 'Canceled'),
    )

    showtimes = models.ForeignKey('Showtimes')
    user = models.ForeignKey('User')
    status = models.IntegerField(
        choices=ORDER_STATUS_CHOICES,
        default=UNCOMFIRMED,
    )
    combo = models.ForeignKey('Combo', null=True, blank=True)
    
class OrderMeal(models.Model):
    meal = models.ForeignKey('Meal')
    order = models.ForeignKey('Order')

class SeatsOrder(models.Model):
    seat = models.ForeignKey('Seat')
    order = models.ForeignKey('Order')

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    account = models.CharField(max_length=25)
    password = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=25)
    birthday = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)
    vip = models.CharField(db_column='VIP', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'










