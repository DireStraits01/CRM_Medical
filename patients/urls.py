from django.urls import path
from . import views

urlpatterns = [
    path('', views.patients, name='patients'),
    path('create_patient/', views.create_patient, name='create_patient'),
    path('update_patient/<int:pk>/', views.update_patient, name='update_patient'),
    path('delete_patient/<int:pk>/', views.delete_patient, name='delete_patient'),
]
