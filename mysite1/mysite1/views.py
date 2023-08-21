from django.http import HttpResponse
from django.shortcuts import render

def aboutUS(request):
    return HttpResponse('Welcom to mysite')

def homepage(request):
    data={
        'title':'Home new',
        'clist':['OS','DC','SWE','DB'],
        'student_details':[
            {'name':'ayesha','phone':1776506703},
            {'name':'shorna','phone':1987852436}
        ]
    }
    return render(request,"index.html",data) 
def courses(req):
    return HttpResponse("All courses")
def courseDetails(req, courseid):
    return HttpResponse(courseid)