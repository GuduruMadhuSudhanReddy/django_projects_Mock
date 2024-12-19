from django.shortcuts import render
import datetime
# Create your views here.
def info_view(request):
    date=datetime.datetime.now()
    name="django"
    prerequisite='python'
    my_dict={'time':date,'name':name, 'prerequisite':prerequisite}
    return render(request,'testapp/wish.html',my_dict)