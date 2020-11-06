from django.shortcuts import render
from .models import*


def home(request):

    return render(request, 'main/dashboard.html')


def doctor(request):
    return render(request, 'main/doctor.html')


def patient(request):
    return render(request, 'main/patient.html')


def service(request):
    service = Service.objects.all
    return render(request, 'main/service.html', {'service': service})
