from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Vclass.models import Course,Session_Year,CustomUser,Student,Teacher
from django.contrib import messages
from Vclass.models import Course
from django.contrib.auth import get_user_model


@login_required(login_url='/')
def HOME(request):
    student_count = Student.objects.all().count()
    teacher_count = Teacher.objects.all().count()
    course_count = Course.objects.all().count()

    context = {
        'student_count':student_count,
        'teacher_count':teacher_count,
        'course_count':course_count,
    }
    return render(request,'student/home.html',context)