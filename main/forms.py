from django.forms import ModelForm, TextInput, DateTimeInput
from .models import *


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

        widgets = {
            "time_appointment": DateTimeInput(attrs={"placeholder": "гггг-мм-дд чч:мм:сс"}),

        }


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

        widgets = {
            "date_of_treatment": TextInput(attrs={
                "placeholder": "гггг-мм-дд чч:мм:сс"
            })
        }


class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
