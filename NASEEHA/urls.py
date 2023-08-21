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
# from signup.views import signaction
from hospital.views import signup, profile, editprofile, forms
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('',views.homepage, name='homepage'),
    path('login/',views.login_user, name='login'),
    path('services/',views.services, name='services'),
    path('signup/',views.signup, name='signup'),
    path('signaction/',signup, name='signaction'),
    path('authenticate_userp/',views.authenticate_userp),
    path('user_profile/',profile,name='user_profile'),
    path('edit_profile/',editprofile, name='edit_profile'),
    path('survey/',forms, name='survey')
]
