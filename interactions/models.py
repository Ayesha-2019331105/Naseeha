from django.db import models
from doctors.models import *
from hospital.models import *

# Create your models here.


class appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    appointment_date = models.DateField(null=True, blank=True)
    appointment_time = models.TimeField(null=True, blank=True)
    appointment_status = models.CharField(
        max_length=70, null=True, blank=True, default='Pending')
    serial_number = models.IntegerField(null=True, blank=True)
    doctor = models.ForeignKey(
        doctor_info, on_delete=models.CASCADE, null=True, blank=True, related_name='doctor')
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, null=True, blank=True, related_name='patient')


class review(models.Model):
    review_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    doctor = models.ForeignKey(
        doctor_info, on_delete=models.CASCADE, null=True, blank=True)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, null=True, blank=True)
