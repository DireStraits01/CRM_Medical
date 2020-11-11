from django.forms import ModelForm
from .models import Appointment, Service, Doctor


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
