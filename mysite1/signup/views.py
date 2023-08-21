from django.shortcuts import render
import mysql.connector as sql
from .models import Contact
fn=''
ln=''
s=''
em=''
pwd=''
# Create your views here.
def signaction(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="ayesha105",database='mysqltutorial')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="sex":
                s=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="insert into users Values('{}','{}','{}','{}','{}')".format(fn,ln,s,em,pwd)
        cursor.execute(c)
        m.commit()

    return render(request,'signup.html')

def contact(request):
    if request.method=='POST':
        full_name=request.POST['full_name']
        email=request.POST['email']
        message=request.POST['message']
        contact=Contact.objects.create(full_name=full_name,email=email,message=message)
        contact.save()
        # messages.success(request,'Data has been submitted')
    return render(request,'contact.html')