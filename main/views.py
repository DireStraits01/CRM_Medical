from django.shortcuts import render
from .models import*
from django.db.models import Sum
import datetime


def home(request):
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    service_check = Service.objects.filter(
        date_of_treatment__gte=today, date_of_treatment__lt=tomorrow)
    total_service_today = service_check.count()
    total_price = service_check.aggregate(Sum('price'))
    total_price_today = float(total_price['price__sum'])
    context = {'service_check': service_check,
               'total_price_today': total_price_today}
    return render(request, 'main/dashboard.html', context)


def doctor(request):
    return render(request, 'main/doctor.html')


def patient(request):
    return render(request, 'main/patient.html')


def service(request):
    service = Service.objects.all
    return render(request, 'main/service.html', {'service': service})


def appointment(request):

    return render(request, 'main/appointment.html')
