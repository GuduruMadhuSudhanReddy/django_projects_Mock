from django.shortcuts import render
from testapp.forms import StudentForm

# Create your views here.
def student_input_view(request):
    submitted = False  # Initialize outside of POST block
    sname = ''  # Initialize outside of POST block
    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            print('Form validation is successful')
            print('Name:', form.cleaned_data['name'])
            print('Rollno:', form.cleaned_data['rollno'])
            print('Marks:', form.cleaned_data['marks'])
            
            submitted = True  # Set submitted to True if form is valid
            sname = form.cleaned_data['name']  # Assign name from form data
    else:
        form = StudentForm()  # For GET requests, return a blank form
    
    return render(request, 'testapp/input.html', {'form': form, 'submitted': submitted, 'sname': sname})
