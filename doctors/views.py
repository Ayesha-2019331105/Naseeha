from django.shortcuts import render

# Create your views here.


def doctorBase(request):
    return render(request, "doctorBase.html")


def doctor_profile(request):
    return render(request, "doctor_profile.html")


def doctor_edit_profile(request):
    return render(request, "doctordetails/doc_editprofile.html")


def patientlist(request):
    return render(request, "doctordetails/patientlist.html")
