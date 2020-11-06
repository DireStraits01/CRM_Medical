from django.shortcuts import render
from .models import*
import datetime


def home(request):
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    service_check = Service.objects.filter(
        date_of_treatment__gte=today, date_of_treatment__lt=tomorrow)
    return render(request, 'main/dashboard.html', {'service_check': service_check})


def doctor(request):
    return render(request, 'main/doctor.html')


def patient(request):
    return render(request, 'main/patient.html')


def service(request):
    service = Service.objects.all
    return render(request, 'main/service.html', {'service': service})


def appointment(request):

    return render(request, 'main/appointment.html')
