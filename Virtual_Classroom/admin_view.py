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
    return render(request,'admin/home.html',context)

@login_required(login_url='/')
def ADD_STUDENT(request):
    course = Course.objects.all()
    session_year = Session_Year.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        student_id = request.POST.get('student_id')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        mobile_number = request.POST.get('mobile_number')
        address = request.POST.get('address')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')
        password = request.POST.get('password')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email is already registered')
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'username is already registered')
            return redirect('add_student')

        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=3
            )
            user.set_password(password)
            user.save()




            course = Course.objects.get(id = course_id)
            session_year = Session_Year.objects.get(id = session_year_id)

            student = Student(
                admin = user,
                student_id = student_id,
                gender = gender,
                date_of_birth = date_of_birth,
                mobile_number = mobile_number,
                address = address,
                course_id = course,
                session_year_id = session_year
            )

            student.save()
            messages.success(request,'Records saved succesfully')
            return redirect('add_student')

    context = {
        'course':course,
        'session_year':session_year,
    }

    return render(request,'admin/add_student.html',context)


def VIEW_STUDENT(request):
    student = Student.objects.all()

    context = {
        'student':student,
    }
    return render(request,'admin/view_student.html',context)


def EDIT_STUDENT(request):
    return render(request,'admin/edit_student.html')


def ADD_COURSE(request):
    if request.method == "POST":
        course_name = request.POST.get('course_name')
        course_id = request.POST.get('course_id')
        course_description = request.POST.get('course_description')




        course = Course(
            name = course_name,
            course_id = course_id,
            course_description = course_description,
        )
        course.save()
        messages.success(request,'Course added successfully')
        return redirect('add_course')

    return render(request,'admin/add_course.html')


def VIEW_COURSE(request):
    course = Course.objects.all()
    context = {
        'course':course,
    }
    return render(request,'admin/view_course.html',context)

@login_required(login_url='/')
def ADD_TEACHER(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        teacher_id = request.POST.get('teacher_id')
        gender = request.POST.get('gender')
        mobile_number = request.POST.get('mobile_number')
        course_taken = request.POST.get('course_taken')
        password = request.POST.get('password')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email is already registered')
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'username is already registered')
            return redirect('add_teacher')

        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=2
            )
            user.set_password(password)
            user.save()




            teacher = Teacher(
                admin = user,
                teacher_id = teacher_id,
                gender = gender,
                mobile_number = mobile_number,
                course_taken = course_taken,
            )

            teacher.save()
            messages.success(request,'Records saved succesfully')
        return redirect('add_teacher')
    return render(request,'admin/add_teacher.html')


def VIEW_TEACHER(request):
    teacher = Teacher.objects.all()
    context = {
        'teacher': teacher,
    }
    return render(request, 'admin/view_teacher.html', context)


def MY_COURSE(request):
    course = Course.objects.all()
    context = {
        'course': course,
    }
    return render(request,'admin/my_course.html')