from django.shortcuts import render, redirect
from main.models import Patient
from main.forms import PatientForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


@login_required(login_url='login')
def patients(request):
    patients = Patient.objects.all()
    context = {'patients': patients}
    return render(request, 'patients/patients.html', context)


############## buttons for patient.html page#########################

@login_required(login_url='login')
def create_patient(request):
    form = PatientForm()
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/patients')
    context = {'form': form}
    return render(request, 'patients/f_patient.html', context)


@login_required(login_url='login')
def update_patient(request, pk):
    patient = Patient.objects.get(id=pk)
    form = PatientForm(instance=patient)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('/patients')
    context = {'form': form}
    return render(request, 'patients/f_patient.html', context)


@login_required(login_url='login')
def delete_patient(request, pk):
    patient = Patient.objects.get(id=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('/patients')
    context = {'patient': patient}
    return render(request, 'patients/delete_patient.html', context)
