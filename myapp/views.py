from datetime import datetime
from django.shortcuts import render,HttpResponse
from .models import *
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,"index.html")


def all_emp(request):
    emps=employee.objects.all()
    context={
        "emps":emps
    }
    return render(request,"view_all_emp.html",context)

def add_emp(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        phone=int(request.POST['phone'])
        dept=int(request.POST['dept'])
        role=int(request.POST['role'])
        new=employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept_id=dept,role_id=role,hire_data=datetime.now())
        new.save()
        return HttpResponse("THANK YOU FOR ADDING VALUE")
    
    else:
        return render(request,"add_emp.html")

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("succesfully deleted")
        except:
            return HttpResponse("NNOT EXIST USER")
    emps=employee.objects.all()
    context={
        "emps":emps
    }
    return render(request,"remove_emp.html",context)

def filter_emp(request):
    if request.method=="POST":
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps=employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps=emps.filter(dept__name=dept)
        if role:
            emps=emps.filter(role__name=role)
        context={
            'emps':emps
        }
        return render(request,"view_all_emp.html",context)
    
    return render(request,"filter_emp.html")

