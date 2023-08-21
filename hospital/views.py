from django.shortcuts import render
# from django.contrib.auth import login,logout,authenticate
# from django.contrib.auth.models import User
from .models import Patient
# from .forms import PatientForm,CustomUserCreationForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def signup(request):
    # form = CustomUserCreationForm()
    #     form = CustomUserCreationForm(request.POST)
    #     if form.is_valid():
    #         user = form.save(commit = False)
    #         user.role = True
    #         user.save()
    #     else:
    #         return render(request,'signup.html')
    print("hhhhh")
    if request.method == "POST":
        print("gggg")
        name = request.POST.get('username')
        age = request.POST.get('age')
        sex = request.POST.get('gender')
        if sex == "female":
            sex = 1
        else:
            sex = 0
        address = request.POST.get('address')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')
        if role == "patient":
            role = 1
        else:
            role = 0
        user = Patient.objects.create(username=name,age=age,sex=sex,
                                      address=address,email=email,password=password,role=role)
        user.save()
        print("here in patien")
    return render(request,'signup.html')

# def get_cur_user()
@csrf_exempt
def profile(request):
    return render(request,"profile.html")

@csrf_exempt
def editprofile(request):
    return render(request,"editprofile.html")

def forms(request):
    return render(request,"forms.html")