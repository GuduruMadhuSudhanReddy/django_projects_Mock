from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display(request):
    s="helolo students welcoe=me to mahesh sir django clases"
    return HttpResponse(s)