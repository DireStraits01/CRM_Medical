import django_filters
from .models import *


class ServiceFilter(django_filters.FilterSet):
    class Meta:
        model = Service
        fields = '__all__'
