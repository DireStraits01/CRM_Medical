from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('doctor_detail/<int:pk>/', views.doctor, name='doctor_detail'),
    path('patient/', views.patient, name='patient'),
    path('service/', views.service, name='service'),
    path('staff/', views.staff, name='staff'),
    path('appointment/', views.appointment, name='appointment'),
    path('create_appointment/', views.create_appointment,
         name='create_appointment'),
    path('updateAppointment/<int:pk>/',
         views.updateAppointment, name='updateAppointment'),
    path('deleteAppointment/<int:pk>/',
         views.deleteAppointment, name='deleteAppointment'),

]
