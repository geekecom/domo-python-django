from django.contrib.auth import logout
from django.shortcuts import render, redirect
from rest_framework import permissions
from rest_framework import viewsets

from domo.serializers import ControlSerializer
from .models import Control
from domo.scripts import bme280_temperature


def index(request):
    control_list = Control.objects.order_by('-name')
    climate_list = bme280_temperature.main()
    temperature = climate_list[0]
    pressure = climate_list[1]
    humidity = climate_list[2]
    context = {'control_list': control_list,
               'temperature': temperature,
               'pressure': pressure,
               'humidity': humidity,
               }
    return render(request, 'controls/index.html', context)


class ControlViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Controls to be viewed or edited.
    """
    queryset = Control.objects.all().order_by('-name')
    serializer_class = ControlSerializer
    permission_classes = [permissions.IsAuthenticated]


def redirect_to_login(request):
    return redirect('/accounts/login/')


def logout_and_redirect(request):
    logout(request)
    return redirect_to_login(request)
