from django.shortcuts import redirect, render
# from django.contrib.auth import login,logout,authenticate
# from django.contrib.auth.models import User
from .models import *
from doctors.models import *
from interactions.models import *
# from .forms import PatientForm,CustomUserCreationForm
from django.views.decorators.csrf import csrf_exempt

# # Create your views here.
# @csrf_exempt
# def signup(request):
#     # form = CustomUserCreationForm()
#     #     form = CustomUserCreationForm(request.POST)
#     #     if form.is_valid():
#     #         user = form.save(commit = False)
#     #         user.role = True
#     #         user.save()
#     #     else:
#     #         return render(request,'signup.html')
#     print("hhhhh")
#     if request.method == "POST":
#         print("gggg")
#         name = request.POST.get('username')
#         age = request.POST.get('age')
#         sex = request.POST.get('gender')
#         if sex == "female":
#             sex = 1
#         else:
#             sex = 0
#         address = request.POST.get('address')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         role = request.POST.get('role')
#         if role == "patient":
#             role = 1
#         else:
#             role = 0
#         user = Patient.objects.create(username=name,age=age,sex=sex,
#                                       address=address,email=email,password=password,role=role)
#         user.save()
#         print("here in patien")
#     return render(request,'signup.html')

# def get_cur_user()


@csrf_exempt
def profile(request):
    return render(request, "profile.html")


def editprofile(request):
    return render(request, "editprofile.html")


@csrf_exempt
def handle_editprofile(request):
    if request.method == "POST":
        cur_user = Patient.objects.get(email=request.POST.get('email'))
        cur_user.name = request.POST.get("name")
        cur_user.address = request.POST.get("address")
        cur_user.blood_group = request.POST.get("blood_group")
        cur_user.phone_number = request.POST.get("mobile_number")
        cur_user.dob = request.POST.get("dob")
        # cur_user.login_status = request.POST.get("offline")
        cur_user.save()
    return redirect('user_profile')


def assign_dept(request):
    dept_list = ['Psychiatry', 'Clinical Psychology', 'Therapy',
                 'Neuropsychology', 'Drug Addiction Treatment', 'Trauma Center']
    print(request.session['cur_hospital'])
    name = Hospital_Information.objects.get(
        name=request.session['cur_hospital'])
    for i in dept_list:
        hospital_dept = hospital_department.objects.create(
            hospital_department_name=i,
            hospital=name,
        )
        print(hospital_dept)
    return redirect('admin_profile')


@csrf_exempt
def save_hospital(request):
    print("jdf")
    if (request.method == "POST"):
        email = request.POST.get('email')
        print(email)
        hospital = Hospital_Information.objects.all()
        dup = False
        for item in hospital:
            if (item.email == email):
                dup = True
                print('hospital already added')
                return redirect('admin_profile')
        if (not (dup)):
            print('in save')
            hospital1 = Hospital_Information.objects.create(
                name=request.POST.get("name"),
                address=request.POST.get("address"),
                email=request.POST.get("email"),
                phone_number=request.POST.get("hotline"),
                hospital_type=request.POST.get("hospital_type"),
                general_bed_no=request.POST.get("general_bed_no"),
                available_icu_no=request.POST.get("available_bed_no"),
                regular_cabin_no=request.POST.get("regular_cabin_no"),
                emergency_cabin_no=request.POST.get("emergency_cabin_no"),
                vip_cabin_no=request.POST.get("vip_cabin_no"),
            )
            hospital1.save()
            request.session['cur_hospital'] = request.POST.get('name')
            print(request.session['cur_hospital'])
            return redirect('assign_dept')
    return redirect('admin_profile')


def forms(request):
    return render(request, "forms.html")


def appointment_list(request):
    patient_info = Patient.objects.get(email=request.GET['pid'])
    apnt = appointment.objects.select_related(
        'patient', 'doctor').filter(patient=patient_info)
    context = {
        'patient_info': patient_info,
        'apnt': apnt,
    }
    return render(request, "appointment_details_p.html", context)


def hospital(request):
    hospital_info = Hospital_Information.objects.all()
    context = {
        'h_info': hospital_info,
    }
    return render(request, "hospital.html", context)


def hospitaldetails(request):
    h_info = Hospital_Information.objects.get(name=request.GET['name'])
    dept = hospital_department.objects.filter(hospital=h_info)
    doc = doctor_info.objects.filter(
        work_place=h_info, department_name__in=dept)
    context = {
        'h_info': h_info,
        'dept': dept,
        'doc': doc,
    }
    return render(request, "hospitaldetails.html", context)


def hos_dept_wise_doc(request):
    h_info = Hospital_Information.objects.get(
        name=request.GET['hospital_name'])
    dept = hospital_department.objects.filter(hospital=h_info)
    dept1 = hospital_department.objects.get(
        hospital_department_name=request.GET['dept_name'],
        hospital=h_info)
    print(dept1)
    doc = doctor_info.objects.filter(
        work_place=h_info, department_name=dept1)
    context = {
        'h_info': h_info,
        'dept': dept,
        'dept1': dept1,
        'doc': doc,
    }
    return render(request, "hospital_department_wise_doctor/dept_wise_doctor.html", context)
