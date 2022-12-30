from django.shortcuts import render, HttpResponse,redirect
from emp_app.models import Employee

# Create your views here.

def index(request):
    # return HttpResponse('This is Index')
    emps=Employee.objects.all()

    return render(request, 'index.html',context={"emps": emps})


def add_emp(request):
    if request.method=='POST':
        name=request.POST.get('name')
        emp_id=request.POST.get('emp_id')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        working=request.POST.get('working')
        department=request.POST.get('department')

        # creat model object end save data

        # another way of creating an object
        e=Employee()
        e.name=name
        e.emp_id=emp_id
        e.email=email
        e.phone=phone
        if working is None:
            e.working=True
        else:
            e.working=False
        e.department=department
        e.save()

        # e=Employee(name=name,emp_id=emp_id,email=email,phone=phone,department=department)
        # e.save()
        return redirect('/')
    return render(request, 'add_emp.html')


def more(request):
    return render(request, 'more.html')

def delete_emp(request,emp_id):
    d_emp=Employee.objects.get(pk=emp_id)
    d_emp.delete()
    return redirect('/')

def update_emp(request,emp_id):
    u_emp=Employee.objects.get(pk=emp_id)
    return render(request,'update.html',context={'u_emp':u_emp})

def do_update_emp(request,emp_id):
    if request.method=='POST':
        name=request.POST.get('name')
        emp_id_temp=request.POST.get('emp_id')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        working=request.POST.get('working')
        department=request.POST.get('department')

    e=Employee.objects.get(pk=emp_id)
    e.name=name
    e.emp_id=emp_id_temp
    e.email=email
    e.phone=phone
    if working is None:
        e.working=True
    else:
        e.working=False
    e.department=department
    e.save()
    return redirect('/')