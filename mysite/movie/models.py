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
