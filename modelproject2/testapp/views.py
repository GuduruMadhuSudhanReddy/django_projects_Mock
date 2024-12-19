from django.shortcuts import render
from testapp.models import Employee
def empdata_view(request):
    emp_list = Employee.objects.all()#select * from employee;
    my_dict = {'emp_list':emp_list}
    return render(request,'testapp/emp.html',my_dict)

# Create your views here.
