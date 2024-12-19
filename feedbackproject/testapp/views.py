from django.shortcuts import render
from testapp.forms import FeedBackForm
# Create your views here.
def feedback_view(request):
    submitted=False
    sname ='' 
    form =FeedBackForm()
    if request.method =='POST':
        form =FeedBackForm(request.POST)
        if form.is_valid():
            print('Form validation success and printing feedback information')
            print('*' *55)
            print('Name:',form.cleaned_data['name'])
            print('Rollno:',form.cleaned_data['rollno'])
            print('EmailID:',form.cleaned_data['email'])
            print('Feedback:',form.cleaned_data['feedback'])
    
            submitted=True
            sname=form.cleaned_data['name']
        else:
           print('some field validate fails')
    return render(request,'testapp/feedback.html',   {'form':form,'submitted':submitted,'sname':sname})

