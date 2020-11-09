from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('doctor/<int:pk>/', views.doctor, name='doctor'),
    path('patient/', views.patient, name='patient'),
    path('service/', views.service, name='service'),
    path('appointment/', views.appointment, name='appointment'),
    path('create_appointment/', views.create_appointment,
         name='create_appointment'),
    # path('appoint_update/<str:pk>/', views.appoint_update, name='appoint_update'),
]
