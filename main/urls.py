from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', views.home, name='admin'),
    path('', views.home, name='home'),
    path('update_home/<int:pk>/', views.update_home, name='update_home'),
    path('delete_home/<int:pk>/', views.delete_home, name='delete_home'),
    path('create_service_home', views.create_service_home,
         name='create_service_home'),

    ##################________Registration|Logo__________#################
    path('reset_password/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
