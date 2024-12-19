from django.urls import path
from . import views

urlpatterns = [
    path('exam/', views.exam_view),
    path('fee/', views.fee_view),
    path('attendence/', views.attendence_view),  
]