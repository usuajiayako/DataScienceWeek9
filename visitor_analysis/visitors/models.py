from django.db import models

# Create your models here.

class Visitor(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length = 2)
    date = models.DateTimeField(auto_now_add = True)
    thumb = models.ImageField(default = 'default.png', blank = True)

    # def __int__(self):
    #     return self.id