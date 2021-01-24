from django.shortcuts import render, redirect
from main.models import Appointment
from main.forms import AppointmentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


@login_required(login_url='login')
def appointment(request):
    appointment = Appointment.objects.all().order_by('time_appointment')
    context = {'appointment': appointment}
    return render(request,  'appointment/appointment.html', context)


##### for create button to appoitment  page##############################
@login_required(login_url='login')
def create_appointment(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/appointment')
    context = {'form': form}
    return render(request, 'appointment/f_appointment.html', context)


@login_required(login_url='login')
def updateAppointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    form = AppointmentForm(instance=appointment)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('/appointment')
    context = {'form': form}
    return render(request, 'appointment/f_appointment.html',  context)


@login_required(login_url='login')
def deleteAppointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    if request.method == "POST":
        appointment.delete()
        return redirect('/appointment')
    context = {'point': appointment}
    return render(request, 'appointment/delete_appointment.html', context)
