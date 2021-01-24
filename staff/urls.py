from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff, name='staff'),
    path('doctor_detail/<int:pk>/', views.doctor, name='doctor_detail'),
    path('create_doctor', views.create_doctor, name='create_doctor'),
    path('update_doctor/<int:pk>/', views.update_doctor, name='update_doctor'),
    path('delete_doctor/<int:pk>/', views.delete_doctor, name='delete_doctor'),

]
