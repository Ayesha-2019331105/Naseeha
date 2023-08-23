from django.shortcuts import render, redirect
from .models import *
from doctors.models import *
from hospital.models import *

# Create your views here.


def request_appointment(request):
    doc = doctor_info.objects.get(email=request.GET['did'])
    patient = Patient.objects.get(email=request.GET['pid'])
    apnt = appointment.objects.create(
        doctor=doc,
        patient=patient,
    )
    context = {
        'pid': patient,
        'doc': doc,
        'apnt': apnt,
    }
    return render(request, 'appointment_details_p.html', context)


def appointment_details(request):
    doc = doctor_info.objects.get(
        email=request.session['cur_doc'].get('email'))
    apnt = appointment.objects.filter(doctor=doc)
    context = {
        'apnt': apnt,
    }
    return render(request, 'appointment_details.html', context)
