from django.forms import ModelForm
from .models import *


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
