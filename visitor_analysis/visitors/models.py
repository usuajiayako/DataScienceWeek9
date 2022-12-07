from django.db import models
from django.contrib.auth.models import User

# Create your models here.
AGE_CHOICE = [
    (0, "under 5"),
    (5, "5 - 9"),
    (10, "10 - 14"),
    (15, "15 - 19"),
    (20, "20 - 30"),
    (30, "30 - 40"),
    (40, "40 - 50"),
    (50, "50 - 60"),
    (60, "above 60"),
]

GENDER_CHOICES = [
    ("F", "Female"),
    ("M", "Male"),
    ]

class Visitor(models.Model):
    age = models.IntegerField(choices=AGE_CHOICE)
    gender = models.CharField(max_length = 2, choices = GENDER_CHOICES)
    date = models.DateTimeField(auto_now_add = True)
    thumb = models.ImageField(default = 'default.png', blank = True)
    user = models.ForeignKey(User, default = None, on_delete=models.CASCADE)

    # def __int__(self):
    #     return self.id