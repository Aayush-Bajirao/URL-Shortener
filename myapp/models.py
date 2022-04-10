from enum import auto
from django.db import models

class LongToShort(models.Model):
    long_url = models.URLField(max_length = 5000)
    short_url = models.CharField(max_length = 100, unique = True)
    date = models.DateField(auto_now_add = True)
    clicks = models.IntegerField(default = 0)

#After Changes in model.py DO THESE STEPS IMIDEITLY
#1.Close server on cmd
#2.pyhton manage.py makemigrations
#3.python manage.py migrate
#Model made are in python but we have to change it into SQL language