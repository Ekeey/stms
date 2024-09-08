from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse 
 
from .models import Student 
 
# Create your views here.
def index(request):
  return render(request, 'students/index.html', {
    'students': Student.objects.all()
  })
  
  
  #def dashboard_view(request):
   # return render(request, 'dashboard.html')

def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponse('view students')

