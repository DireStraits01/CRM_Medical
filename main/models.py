from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)
    phone = models.CharField(max_length=12, null=True, blank=True)
    email = models.CharField(max_length=20, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=50)
    treatment_doctor = models.ForeignKey(
        Doctor, related_name='treatment_doctor', on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, null=True, blank=True)
    email = models.CharField(max_length=20, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    patient = models.ForeignKey(
        Patient, related_name='patient', on_delete=models.CASCADE)

    treatment = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.CharField(max_length=30)
    date_of_treatment = models.DateTimeField()

    def __str__(self):
        return self.treatment, self.price, self.patient
