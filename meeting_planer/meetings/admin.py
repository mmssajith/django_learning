from django.contrib import admin

# Register your models here.
from .models import Meetings
from .models import Room

admin.site.register(Meetings)
admin.site.register(Room)