from django.shortcuts import render, redirect
from main.models import Doctor
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from main.forms import DoctorForm


@login_required(login_url='login')
def staff(request):
    staff = Doctor.objects.all()
    context = {'staff': staff}
    return render(request, 'staff/staff.html', context)


@login_required(login_url='login')
def doctor(request, pk=0):
    doctor = Doctor.objects.get(id=pk)
    services = doctor.attending_doctor.all()
    count_service = services.count()
    # staff = Doctor.objects.all()
    context = {'doctor': doctor,
               'count_service': count_service, }
    return render(request, 'staff/doctor_detail.html', context)


############## buttons for staff.html page#########################

@login_required(login_url='login')
def create_doctor(request):
    form = DoctorForm()
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/staff')
    context = {'form': form}
    return render(request, 'staff/f_doctor.html', context)


@login_required(login_url='login')
def update_doctor(request, pk):
    doctor = Doctor.objects.get(id=pk)
    form = DoctorForm(instance=doctor)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('/staff')
    context = {'form': form}
    return render(request, 'staff/f_doctor.html', context)


@login_required(login_url='login')
def delete_doctor(request, pk):
    doctor = Doctor.objects.get(id=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('/staff')
    context = {'employee': doctor}
    return render(request, 'staff/delete_doctor.html', context)
