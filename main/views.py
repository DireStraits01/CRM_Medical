from django.shortcuts import render, redirect
from .models import Service, Appointment
import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import ServiceForm, AppointmentForm
from django.db.models import Sum
from django.db.models.functions import Coalesce


@login_required(login_url='login')
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
    return render(request, 'main/index.html', context)


##### for create button to home page##############################


@login_required(login_url='login')
def delete_home(request, pk):
    delete_home = Service.objects.get(id=pk)
    if request.method == "POST":
        delete_home.delete()
        return redirect('/')
    context = {'check': delete_home}
    return render(request, 'main/delete_home.html', context)


@login_required(login_url='login')
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


@login_required(login_url='login')
def create_service_home(request):
    form = ServiceForm()
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'main/f_home.html', context)
