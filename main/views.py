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


def doctor(request, pk=0):
    doctor = Doctor.objects.get(id=pk)
    services = doctor.attending_doctor.all()
    count_service = services.count()
    # staff = Doctor.objects.all()
    context = {'doctor': doctor,
               'count_service': count_service, }
    return render(request, 'main/doctor_detail.html', context)


def staff(request):
    staff = Doctor.objects.all()
    context = {'staff': staff}
    return render(request, 'main/staff.html', context)


def patient(request):
    return render(request, 'main/patient.html')


def service(request):
    service = Service.objects.all
    context = {'service': service}
    return render(request, 'main/service.html', context)


def appointment(request):
    after_one_week = Appointment.objects.all
    today = datetime.date.today()
    after_one_week = today + datetime.timedelta(days=15)
    last_week_appointment = Appointment.objects.filter(
        time_appointment__gte=today, time_appointment__lt=after_one_week)
    return render(request, 'main/appointment.html', {'last_week_appointment': last_week_appointment})


def create_appointment(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/appointment')
    context = {'form': form}
    return render(request, 'main/f_appointment.html', context)


def updateAppointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    form = AppointmentForm(instance=appointment)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('/appointment')
    context = {'form': form}
    return render(request, 'main/f_appointment.html',  context)


def deleteAppointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    if request.method == "POST":
        appointment.delete()
        return redirect('/appointment')
    context = {'point': appointment}
    return render(request, 'main/delete_appointment.html', context)
