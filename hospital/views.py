from django.shortcuts import redirect, render
# from django.contrib.auth import login,logout,authenticate
# from django.contrib.auth.models import User
from .models import Patient, UserP
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


def forms(request):
    return render(request, "forms.html")


def hospital(request):
    return render(request, "hospital.html")


def hospitaldetails(request):
    return render(request, "hospitaldetails.html")
