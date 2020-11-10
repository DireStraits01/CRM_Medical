from django.forms import ModelForm
from .models import Appointment, Service


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ('patient', 'attending_doctor', 'price', 'date_of_treatment')
