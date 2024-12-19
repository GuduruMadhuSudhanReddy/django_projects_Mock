from django.shortcuts import render

# Create your views here.
def news_info(request):
    return render(request,'testapp/index.html')
def movies_info(request):
       head_msg="Movies information"
       sub_msg1="Devara is awesome"
       sub_msg2="planining for the shoooting  of the devara"
       sub_msg3="dont gor the movies stdy the Django"
       type='Movies'
       my_dict={'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
       return render(request,'testapp/news.html',my_dict)
def sports_info(request):
       head_msg="Sports information"
       sub_msg1="india is awesome"
       sub_msg2="planining for the next  oneday  world cup"
       sub_msg3="dont gor the sports stdy the Django"
       type='Sports'
       my_dict={'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
       return render(request,'testapp/news.html',my_dict)
def politics_info(request):
       head_msg="politics information"
       sub_msg1="jagan is biggest politician "
       sub_msg2="planining for the next  election campnying  p"
       sub_msg3="dont gor the politicss  study the Django"
       type='Politics'
       my_dict={'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
       return render(request,'testapp/news.html',my_dict)