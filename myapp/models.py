from datetime import datetime
from enum import unique
from unittest.util import _MAX_LENGTH
from xml.dom.minidom import CharacterData
from django.db import models
from django.forms import CharField

class LongToShort(models.Model):
    long_url = models.URLField(max_length = 5000)
    short_url = CharacterData(max_length = 100, unique = True)
    date = models.DateField(auto_now_add = True)
    clicks = models.IntegerField(default = 0)
