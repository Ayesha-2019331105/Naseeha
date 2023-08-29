from django.shortcuts import render, redirect
from .models import *
from doctors.models import *
from hospital.models import *
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def request_appointment(request):
    if request.method == "POST":
        doc = doctor_info.objects.get(email=request.POST.get('email'))
        date = request.POST.get('date')
        print(date)
        patient = Patient.objects.get(
            email=request.session['cur_user'].get('email'))
        apnt1 = appointment.objects.create(
            doctor=doc,
            patient=patient,
            appointment_date=date,
        )
        apnt1.save()
        apnt = appointment.objects.filter(patient=patient)
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
        print(request.POST.get('aid'))
        print(request.POST.get('sl'))
        apnt = appointment.objects.get(appointment_id=request.POST.get('aid'))
        if (apnt.appointment_date is None):
            apnt.appointment_date = request.POST.get('date')
        apnt.serial_number = request.POST.get('sl')
        if (apnt.appointment_time is None):
            apnt.appointment_time = request.POST.get('time')
        if (apnt.appointment_status == "Pending"):
            apnt.appointment_status = request.POST.get('status')
        apnt.save()
        print(apnt)
        return redirect('doctor_profile')
    return redirect('doctor_profile')


@csrf_exempt
def save_feedback(request):
    if request.method == "POST":
        doc_email = request.session['doc_email']
        print(doc_email, "mail")
        doctor = doctor_info.objects.get(
            email__in=doc_email, username=request.POST['doc_name'])
        p = Patient.objects.get(email=request.session['cur_user'].get('email'))
        feedback = review.objects.create(
            doctor=doctor,
            patient=p,
            title=str(request.POST['ratings']),
            message=request.POST['feedback_text'],
        )
    return redirect('user_profile')
