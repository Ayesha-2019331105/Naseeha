from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from hospital.models import Patient, UserP
# from hospital.views import signup
from doctors.models import doctor_info
from django.views.decorators.csrf import csrf_exempt


def homepage(request):
    return render(request, "index.html")


def services(request):
    return render(request, "services.html")


def login_user(request):
    return render(request, 'login_user.html')


def admin_profile(request):
    return render(request, 'admin_user.html')


def add_hospital(request):
    return render(request, 'add_hospital.html')


@csrf_exempt
def logout(request):
    print('here')
    if request.method == "POST":
        print('inside here')
        cur_user = UserP.objects.get(
            email=request.session['cur_user'].get('email'))
        cur_user.login_status = 0
        cur_user.save()
        if cur_user.role:
            cur_user = Patient.objects.get(
                email=request.session['cur_user'].get('email'))
            cur_user.login_status = 'offline'
            cur_user.save()
        else:
            cur_user = doctor_info.objects.get(
                email=request.session['cur_user'].get('email'))
            cur_user.login_status = 'offline'
            cur_user.save()
    return redirect('login')


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
                    cur_user = UserP.objects.get(email=item.email)
                    cur_user.login_status = 1
                    cur_user.save()
                    print("login successfull")
                    if (cur_user.is_superuser):
                        return redirect('admin_profile')
                    if (item.role == 1):
                        cur_user = Patient.objects.get(email=item.email)
                        request.session['cur_user'] = {
                            'username': cur_user.username,
                            'age': cur_user.age,
                            'email': cur_user.email,
                            'password': cur_user.password,
                            'role': cur_user.role,
                            'address': cur_user.address,
                            'name': cur_user.name,
                            'login_status': 'online',
                        }
                        cur_user.login_status = 'online'
                        cur_user.save()
                        return redirect('user_profile')
                    elif (item.role == 0):
                        cur_user = doctor_info.objects.get(email=item.email)
                        request.session['cur_user'] = {
                            'username': cur_user.username,
                            'age': cur_user.age,
                            'email': cur_user.email,
                            'password': cur_user.password,
                            'role': cur_user.role,
                            'address': cur_user.address,
                            'name': cur_user.name,
                            'login_status': 'online',
                            'phone_number': cur_user.phone_number,
                            'nid': cur_user.nid,
                            'visiting_hour': cur_user.visiting_hour,
                            'degree': cur_user.degree,
                            'designation': cur_user.designation,
                            'work_place': cur_user.work_place,
                            'dob': cur_user.dob,
                        }
                        request.session['cur_doc'] = request.session['cur_user']
                        cur_user.login_status = 'online'
                        cur_user.save()
                        return redirect('doctor_profile')
                else:
                    print("wrong password")
                    return redirect('homepage')
        if not (exist_userp):
            print("Invalid email")
            return redirect('signup')
    return render(request, 'login_user.html')


@csrf_exempt
def signup(request):
    cur_user = get_user_model()
    print("cureent_user", cur_user)
    rl = 0
    gender = 0
    if request.POST.get("role") == "patient":
        rl = 1
    if request.POST.get("gender") == "female":
        gender = 1
    print(rl, gender)
    if request.method == "POST":
        new_user = UserP.objects.create(
            username=request.POST.get("username"),
            role=rl,
            login_status=False,
            email=request.POST.get("email"),
            password=request.POST.get("password"),
        )
        print("new_user", new_user)
        new_user.save()
        if request.POST.get("role") == "patient":
            new_user = Patient.objects.create(
                username=request.POST.get("username"),
                age=request.POST.get("age"),
                sex=gender,
                address=request.POST.get("address"),
                email=request.POST.get("email"),
                password=request.POST.get("password"),
                role=rl,
            )
            # print("new_user",new_user)
            new_user.save()
            return redirect("login")
        else:
            new_user = doctor_info.objects.create(
                username=request.POST.get("username"),
                age=request.POST.get("age"),
                gender=gender,
                address=request.POST.get("address"),
                email=request.POST.get("email"),
                password=request.POST.get("password"),
                role=rl,
            )
            return redirect("login")

    return render(request, "signup.html")
