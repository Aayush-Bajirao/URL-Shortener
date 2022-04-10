from django.contrib import admin

from URL_shortner.myapp.models import LongToShort

from .models import LongToShort

admin.site.register(LongToShort)