from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    national_id = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=11)
