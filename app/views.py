from django.shortcuts import render
from .models import Student

def index(request):
    students = Student.objects.all()
    context = {'students':students}
    return render(request, 'index.html', context)

def profile(request, id):
    student = Student.objects.get(id=id)
    context = {'student':student}
    return render(request, 'profile.html', context)