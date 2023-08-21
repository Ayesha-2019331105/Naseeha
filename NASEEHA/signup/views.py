from django.shortcuts import render
import mysql.connector as sql
nm=''
ag=''
s=''
add=''
em=''
pwd=''
rl=''
# Create your views here.
def signaction(request):
    global nm,ag,s,add,em,pwd,rl
    if request.method=="POST":
        m=sql.connect(host="127.0.0.1",user="root",passwd="ayesha105",database='naseeha')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="name":
                nm=value
            if key=="age":
                ag=value
            if key=="sex":
                if value == 'male':
                    s = False
                else:
                    s = True
            if key=="address":
                add=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
            if key=="role":
                if value == 'patient':
                    rl = True
                else:
                    rl = False
        
        c="insert into users Values('{}','{}','{}','{}','{}','{}','{}')".format(nm,ag,s,add,em,pwd,rl)
        cursor.execute(c)
        m.commit()

    return render(request,'signup.html')