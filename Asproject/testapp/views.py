from django.shortcuts import render
import datetime,random
# Create your views here.

def result_view(request):
    msg_list=['the golden days are achead',
    'better to slleep more time even in class',
    'tommorow will be the best day orlife',
    'tommorow is the perfect day to propse ur GF',
    'Very soon we will get the job',]
    names_list=['suunny','radhika','lillly','samanth']
    time= datetime.datetime.now()
    h=int(time.strftime('%H'))
    if h<12:
        s='good Morning'
    elif h<16: 
          s='good afternoon'
    elif h<21:
        s='good evening'     
    else: 
        s='goodnight'  
    name=random.choice(names_list)  
    msg=random.choice(msg_list)
    my_dict={'time':time,'name':name,'msg':msg,'wish':s}
    return render(request,'testapp/result.html',my_dict)  