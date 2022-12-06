from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Visitor(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length = 2)
    date = models.DateTimeField(auto_now_add = True)
    thumb = models.ImageField(default = 'default.png', blank = True)
    user = models.ForeignKey(User, default = None, on_delete=models.CASCADE)

    # def __int__(self):
    #     return self.id