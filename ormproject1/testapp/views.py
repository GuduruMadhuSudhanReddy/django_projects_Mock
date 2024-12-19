from django.shortcuts import render
from testapp.models import Employee
# Create your views here.
def retrieve_view(request):
    emp_list = Employee.objects.all()  # Retrieve all Employee objects from the database.
    print(type(emp_list))  # Outputs the type of emp_list, which is a QuerySet.
    return render(request, 'testapp/index.html', {'emp_list': emp_list})  # Pass the QuerySet to a template.
