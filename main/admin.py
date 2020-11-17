from django.contrib import admin

from .models import *

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Service)
admin.site.register(Treatment)
admin.site.register(Appointment)
