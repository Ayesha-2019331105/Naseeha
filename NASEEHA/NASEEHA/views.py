from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from hospital.models import Patient, UserP
from hospital.views import signup
from doctors.models import doctor_info
from django.views.decorators.csrf import csrf_exempt

def homepage(request):
    return render(request,"index.html")

def services(request):
    return render(request,"services.html")

def login_user(request):
    return render(request,'login_user.html')


@csrf_exempt
def authenticate_userp(request):
    print("dkjfj")
    if request.method == "POST":
        exist_userp = False
        email = request.POST.get('email')
        print(email)
        password = request.POST.get('password')
        user = UserP.objects.all()
        # print(user,"not_null")
        for item in user:
            if item.email == email:
                exist_userp = True

                if item.password == password:
                    print("login successfull")
                    if(item.role == 1):
                        cur_user= Patient.objects.get(email=item.email)
                        request.session['cur_user'] = {
                            'username' : cur_user.username,
                            'age' : cur_user.age,
                            'email' : cur_user.email,
                            'password' : cur_user.password,
                            'role' : cur_user.role,
                            'address':cur_user.address,
                            'name':cur_user.name,
                        }
                        return redirect('user_profile')
                    return redirect('services')
                else:
                    print("wrong password")
                    return redirect('homepage')
        if not(exist_userp):
            print("Invalid email")
            return redirect('signup')
    return render(request,'index.html')

@csrf_exempt
def signup(request):
    cur_user = get_user_model()
    print("cureent_user",cur_user)
    rl = 0
    gender = 0
    if request.POST.get("role") == "patient":
        rl = 1
    if request.POST.get("gender") == "female":
        gender = 1
    print(rl,gender)
    if request.method == "POST":
        new_user = UserP.objects.create(
        username = request.POST.get("username"),
        role = rl,
        login_status = False,
        email = request.POST.get("email"),
        password = request.POST.get("password"),
        )
        print("new_user",new_user)
        new_user.save()
        if request.POST.get("role") == "patient":
            new_user = Patient.objects.create(
            username = request.POST.get("username"),
            age = request.POST.get("age"),
            sex = gender,
            address = request.POST.get("address"),
            email = request.POST.get("email"),
            password = request.POST.get("password"),
            role = rl,
            )
            # print("new_user",new_user)
            new_user.save()
            return redirect("login")
        else:
            new_user = doctor_info.objects.create(
            username = request.POST.get("username"),
            age = request.POST.get("age"),
            gender = gender,
            address = request.POST.get("address"),
            email = request.POST.get("email"),
            password = request.POST.get("password"),
            role = rl,
            )
            return redirect("login")
        # new_user = cur_user(
        #     username = request.POST.get("username"),
        #     age = request.POST.get("age"),
        #     sex = request.POST.get("gender"),
        #     address = request.POST.get("address"),
        #     email = request.POST.get("email"),
        #     password = request.POST.get("password"),
        #     role = request.POST.get("role"),
        # )
        # print("new_user",new_user.get_username(),new_user)
        # render(request,"singup.html")
    
    return render(request,"signup.html")