"""
URL configuration for NASEEHA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from NASEEHA import views
from doctors.views import *
from hospital.views import *
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.homepage, name='homepage'),
    path('login/', views.login_user, name='login'),
    path('services/', views.services, name='services'),
    path('signup/', views.signup, name='signup'),
    path('authenticate_userp/', views.authenticate_userp),
    path('user_profile/', profile, name='user_profile'),
    path('edit_profile/', editprofile, name='editprofile'),
    path('handle_edit_profile/', handle_editprofile, name='handleedit'),
    path('survey/', forms, name='survey'),
    path('logout/', views.logout, name='logout'),
    path("doctorBase/", doctorBase),
    path("doctor_profile/", doctor_profile, name='doctor_profile'),
    path("doctor_edit_profile/", doctor_edit_profile, name='doc_edit_profile'),
    path("patientlist/", patientlist, name='patientlist'),
    path("hospital/", hospital, name="hospital"),
    path("hospitaldetails/", hospitaldetails, name="hospitaldetails"),
]
