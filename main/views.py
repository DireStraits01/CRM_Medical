from django.shortcuts import render, redirect
from .models import*
from django.db.models import Sum
import datetime
from django.db.models.functions import Coalesce
from .forms import AppointmentForm, ServiceForm, DoctorForm


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
    patients = Patient.objects.all()
    context = {'patients': patients}
    return render(request, 'main/patients.html', context)


def service(request):
    if request.method == 'POST':
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        searchresult = Service.objects.raw(
            'select   id,  time_appointment from appointment_db where  time_appointment between "'+fromdate+'" and "'+todate + '"')
        context = {'service': searchresult}
        return render(request, 'main/service.html', context)
    else:
        service = Service.objects.all().order_by('date_of_treatment')
        context = {'service': service}
        return render(request, 'main/service.html', context)


def appointment(request):
    appointment = Appointment.objects.all().order_by('time_appointment')
    context = {'appointment': appointment}
    return render(request,  'main/appointment.html', context)
    # today = datetime.date.today()
    # after_one_week = today + datetime.timedelta(days=15)
    # last_week_appointment = Appointment.objects.filter(
    #     time_appointment__gte=today, time_appointment__lt=after_one_week).order_by('time_appointment')
    # return render(request, 'main/appointment.html', {'last_week_appointment': last_week_appointment})


##### for create button to appoitment  page##############################
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

##### for create button to home page##############################


def delete_home(request, pk):
    delete_home = Service.objects.get(id=pk)
    if request.method == "POST":
        delete_home.delete()
        return redirect('/')
    context = {'check': delete_home}
    return render(request, 'main/delete_home.html', context)


def update_home(request, pk):
    service_home = Service.objects.get(id=pk)
    form = ServiceForm(instance=service_home)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service_home)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'main/f_home.html', context)


def create_service_home(request):
    form = ServiceForm()
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'main/f_home.html', context)


##### for create button to service page##############################

def create_service(request):
    form = ServiceForm()
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/service')
    context = {'form': form}
    return render(request, 'main/f_home.html', context)


def update_service(request, pk):
    service = Service.objects.get(id=pk)
    form = ServiceForm(instance=service)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('/service')
    context = {'form': form}
    return render(request, 'main/f_home.html', context)


def delete_service(request, pk):
    service = Service.objects.get(id=pk)
    if request.method == "POST":
        service.delete()
        return redirect('/service')
    context = {'works': service}
    return render(request, 'main/delete_service.html', context)
############## buttons for staff.html page#########################


def create_doctor(request):
    form = DoctorForm()
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/staff')
    context = {'form': form}
    return render(request, 'main/f_doctor.html', context)


def update_doctor(request, pk):
    doctor = Doctor.objects.get(id=pk)
    form = DoctorForm(instance=doctor)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('/staff')
    context = {'form': form}
    return render(request, 'main/f_doctor.html', context)


def delete_doctor(request, pk):
    doctor = Doctor.objects.get(id=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('/staff')
    context = {'employee': doctor}
    return render(request, 'main/delete_doctor.html', context)
