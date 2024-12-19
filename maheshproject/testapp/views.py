from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def exam_view(request):
    return HttpResponse('<h1> examp view</h1>')
def fee_view(request):
    return HttpResponse('<h1>  fee view</h1>')
def attendence_view(request):
    return HttpResponse('<h1>  attendence view<h1>')