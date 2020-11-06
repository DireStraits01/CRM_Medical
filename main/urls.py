from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('doctor/', views.doctor, name='doctor'),
    path('patient/', views.patient, name='patient'),
    path('service/', views.service, name='service'),
    path('appointment/', views.appointment, name='appointment'),
]
