from django.contrib import admin

from .models import Doctor, Patient, Service, Treatment

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Service)
admin.site.register(Treatment)
