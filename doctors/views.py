from django.shortcuts import redirect, render
from .models import *
# Create your views here.
from hospital.models import *
from django.views.decorators.csrf import csrf_exempt


def doctorBase(request):
    return render(request, "doctorBase.html")


def doctor_profile(request):
    doc_info = doctor_info.objects.get(
        email=request.session['cur_user'].get('email'))
    context = {'doc_info': doc_info}
    return render(request, "doctor_profile.html", context)


def doctor_edit_profile(request):
    # Fetch the hospital info as needed
    hospital_info = Hospital_Information.objects.all()
    dept_list = hospital_department.objects.all()
    context = {
        'hospital_info': hospital_info,
        'dept': dept_list,
    }
    return render(request, "doctordetails/doc_editprofile.html", context)


@csrf_exempt
def handle_doctor_edit_profile(request):
    print("kjjhgf")
    if request.method == "POST":
        cur_user = doctor_info.objects.get(email=request.POST.get('email'))
        print(cur_user.email)
        cur_user.name = request.POST.get("name")
        cur_user.address = request.POST.get("address")
        cur_user.department = request.POST.get("expertise")
        work_place = request.POST.get("work_place")
        hospital_info = Hospital_Information.objects.get(name=work_place)
        dept_name = hospital_department.objects.get(
            hospital_department_name=request.POST.get('dept_name'), hospital=hospital_info.hospital_id)
        cur_user.department_name = dept_name
        cur_user.phone_number = request.POST.get("phone_number")
        cur_user.degree = request.POST.get("degree")
        cur_user.work_place = work_place
        cur_user.designation = request.POST.get("designation")
        cur_user.visiting_hour = request.POST.get("visiting_hour")
        cur_user.nid = request.POST.get("nid")
        cur_user.save()
        return redirect('doctor_profile')
    return redirect('doctor_profile')


def patientlist(request):
    return render(request, "doctordetails/patientlist.html")
