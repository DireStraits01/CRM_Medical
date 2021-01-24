from django.urls import path
from . import views

urlpatterns = [
    path('', views.service, name='service'),
    path('create_service', views.create_service,
         name='create_service'),
    path('update_service/<int:pk>/', views.update_service, name='update_service'),
    path('delete_service/<int:pk>/', views.delete_service, name='delete_service'),

]
