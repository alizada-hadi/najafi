from django.shortcuts import redirect, render
from django.contrib import messages

from employees.models import Employee
from .forms import EmployeeForm
# Create your views here.


def employee_create_view(request):
    if request.method == "POST":
        forms = EmployeeForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request, "Employee created successfully ")
            return redirect("employee-list")
    else:
        forms = EmployeeForm()

    context = {
        'forms' : forms
    }

    return render(request, "employees/employee_form.html", context)



def employee_update_view(request, pk):
    employees = Employee.objects.get(pk=pk)
    if request.method == "POST":
        forms = EmployeeForm(request.POST, request.FILES, instance=employees)
        if forms.is_valid():
            forms.save()
            messages.success(request, "Employee updated successfully")
            return redirect("employee-list")
    else:
        forms = EmployeeForm(instance=employees)
    context={
        "employees": employees,
        "forms": forms
    }
    return render(request, "employees/employee_form.html", context)

def employee_list_view(request):
    employees = Employee.objects.all()
    context={
        'employees': employees
    }
    
    return render(request , 'employees/employee_list.html', context)

def employee_delete_view(request):
    if request.method == "POST":
        id = request.POST.get("employee-id")
        employee = Employee.objects.get(pk=id)
        employee.delete()
    return redirect("employee-list")