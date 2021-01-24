from django.shortcuts import render, redirect
from main.models import Service
from main.forms import ServiceForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum
from django.db.models.functions import Coalesce


@login_required(login_url='login')
def service(request):
    if request.method == 'POST':
        fromdate = request.POST['fromdate']
        todate = request.POST['todate']
        searchresult = Service.objects.filter(
            date_of_treatment__lte=todate, date_of_treatment__gte=fromdate).order_by('date_of_treatment')
        total_price = searchresult.aggregate(
            sum=(Coalesce(Sum('price'), 0)))
        total_price_service = total_price['sum']

        context = {'service': searchresult,
                   'total_price_service': total_price_service}
        return render(request, 'service/service.html', context)
    else:
        service = Service.objects.all().order_by('date_of_treatment')
        total_price = service.aggregate(
            sum=(Coalesce(Sum('price'), 0)))
        total_price_service = total_price['sum']
        context = {'service': service,
                   'total_price_service': total_price_service}
        return render(request, 'service/service.html', context)


##### for create button to service page##############################


@login_required(login_url='login')
def create_service(request):
    form = ServiceForm()
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/service')
    context = {'form': form}
    return render(request, 'main/f_home.html', context)


@login_required(login_url='login')
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


@login_required(login_url='login')
def delete_service(request, pk):
    service = Service.objects.get(id=pk)
    if request.method == "POST":
        service.delete()
        return redirect('/service')
    context = {'works': service}
    return render(request, 'service/delete_service.html', context)
