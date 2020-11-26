from django.contrib import admin

# Register your models here.
from . models import Juego, JuegoInstance

admin.site.register(Juego)
admin.site.register(JuegoInstance)