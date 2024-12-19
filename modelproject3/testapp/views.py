from django.shortcuts import render
from testapp.models import Student
# Create your views here.
def student_view(request):
    #student_list = Student.objects.all()
    #student_list = Student.objects.filter(marks__lt=35)
    #student_list = Student.objects.filter(name__startswith='S')
    student_list = Student.objects.all().order_by('-marks')
    my_dict = {'student_list':student_list}
    return render(request,'testapp/std.html',my_dict)

