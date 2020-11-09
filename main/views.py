from django.shortcuts import render, redirect
from .models import*
from django.db.models import Sum
import datetime
from django.db.models.functions import Coalesce
from .forms import AppointmentForm


def home(request):
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    service_check = Service.objects.filter(
        date_of_treatment__gte=today, date_of_treatment__lt=tomorrow)
    # total_service_today = service_check.count()
    total_price = service_check.aggregate(
        sum=(Coalesce(Sum('price'), 0)))
    total_price_today = total_price['sum']
    context = {'service_check': service_check,
               'total_price_today': total_price_today}
    return render(request, 'main/dashboard.html', context)


def doctor(request, pk):
    doctor = Doctor.objects.get(id=pk)
    services = doctor.attending_doctor.all()
    context = {'doctor': doctor, 'services': services}
    return render(request, 'main/doctor.html', context)


def patient(request):
    return render(request, 'main/patient.html')


def service(request):
    service = Service.objects.all

    # # total_servie = service.aggregate(sum=(Coalesce(Sum('price'), 0)))
    # # totalPriceService = total_servie['sum']
    # context = {'service': service, 'totalPriceService': totalPriceService, }
    return render(request, 'main/service.html',)


def appointment(request):
    after_one_week = Appointment.objects.all
    today = datetime.date.today()
    after_one_week = today + datetime.timedelta(days=15)
    last_week_appointment = Appointment.objects.filter(
        time_appointment__gte=today, time_appointment__lt=after_one_week)
    return render(request, 'main/appointment.html', {'last_week_appointment': last_week_appointment})


def create_appointment(request):
    form = AppointmentForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'main/f_appointment.html', {'form': form})


def appoint_update(request, pk):
    form = AppointmentForm()
    return render(request, 'main/f_appointment.html', {'form': form})
