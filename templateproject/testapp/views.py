from django.shortcuts import render
import datetime
# Create your views here.
def  wish(request):
    date=datetime.datetime.now()
    msg= 'hello guest very good'
    h=int(date.strftime('%H'))
    if h<=12:
        msg+='morning'
    elif h<16:
        msg+='afternoon'  
    elif h<21:
           msg+='evening'    
    else :
         msg+='night'
             

    my_dict={'insert_date':date,'msg':msg}
    return render (request,'testapp/wish.html',my_dict)
  