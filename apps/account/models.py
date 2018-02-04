import random

import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models


def get_random_number():
    return random.randint(1, 100)


class User(AbstractUser):
    birthday = models.DateField('Birthday', default=datetime.date.today)
    number = models.IntegerField('Number', default=get_random_number)
