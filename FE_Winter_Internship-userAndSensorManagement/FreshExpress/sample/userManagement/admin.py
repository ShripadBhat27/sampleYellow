from django.contrib import admin
from .models import Team, Employee, Site

# Register your models here.

admin.site.register(Team)
admin.site.register(Employee)
admin.site.register(Site)
