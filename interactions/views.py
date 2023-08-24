from django.shortcuts import render, redirect
from .models import *
from doctors.models import *
from hospital.models import *
from django.utils import timezone

# Create your views here.


def request_appointment(request):
    doc = doctor_info.objects.get(email=request.GET['did'])
    patient = Patient.objects.get(email=request.GET['pid'])
    apnt = appointment.objects.create(
        doctor=doc,
        patient=patient,
        serial_number=int(timezone.now().timestamp()),
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
    apnt = appointment.objects.select_related(
        'patient', 'doctor').filter(doctor=doc)
    # print(apnt.appointment_id)
    context = {
        'apnt': apnt,
        'doc': doc,
    }
    return render(request, 'doctordetails/appointment.html', context)


def update_appointment(request):
    if (request.method == "POST"):
        apnt = appointment.objects.get(appointment_id=request.POST.get('aid'))
        apnt.appointment_date = request.POST.get('date')
        apnt.appointment_time = request.POST.get('time')
        apnt.appointment_status = request.POST.get('status')
        apnt.save()
        return redirect('doctor_profile')
    return redirect('doc_profile')
