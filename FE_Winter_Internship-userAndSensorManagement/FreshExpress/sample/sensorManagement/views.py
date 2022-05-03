from django.shortcuts import render
from django.http import HttpResponse
from .models import Sensor
from .models import Master
from django.template import loader

# Create your views here.


def sensorView(request):
    masters = Master.objects.all()
    sensors = Sensor.objects.all()
    template = loader.get_template('sensorManagement/sensor.html')
    context = {
        'masters': masters,
        'sensors': sensors,
    }
    return HttpResponse(template.render(context, request))
