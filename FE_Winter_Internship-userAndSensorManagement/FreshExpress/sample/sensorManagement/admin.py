from django.contrib import admin
from .models import Master
from .models import Sensor

# Register your models here.
#Username: django-admin || Password: admin@1234

admin.site.register(Sensor)
admin.site.register(Master)
