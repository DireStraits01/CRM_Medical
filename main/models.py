from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    email = models.CharField(max_length=20, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12, null=True, blank=True)
    email = models.CharField(max_length=20, null=True, blank=True)
    date_created = models.DateTimeField(
        auto_now_add=True)

    def __str__(self):
        return self.name


class Treatment(models.Model):
    type_of_treatment = models.CharField(max_length=50)

    def __str__(self):
        return self.type_of_treatment


class Service(models.Model):
    patient = models.ForeignKey(
        Patient, related_name='patient', null=True, on_delete=models.SET_NULL)
    attending_doctor = models.ForeignKey(
        Doctor, related_name='attending_doctor', null=True, on_delete=models.SET_NULL)
    treatment = models.ForeignKey(
        Treatment, related_name="treatment", null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True, max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_treatment = models.DateTimeField()

    class Meta:
        db_table = "service_db"

    def __str__(self):
        return '%s %s %s' % (self.treatment, self.price, self.attending_doctor)


class Appointment(models.Model):
    time_appointment = models.DateTimeField()
    patient = models.ForeignKey(
        Patient, related_name='patient_to_appointment', null=True, on_delete=models.SET_NULL)
    doctor = models.ForeignKey(
        Doctor, related_name='doctor_appointment', null=True, on_delete=models.SET_NULL)
    complaint = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.time_appointment, self.doctor)
