from django.urls import path
from . import views

urlpatterns = [

    path('', views.appointment, name='appointment'),

    path('create_appointment/', views.create_appointment,
         name='create_appointment'),

    path('updateAppointment/<int:pk>/',
         views.updateAppointment, name='updateAppointment'),

    path('deleteAppointment/<int:pk>/',
         views.deleteAppointment, name='deleteAppointment'),
]
