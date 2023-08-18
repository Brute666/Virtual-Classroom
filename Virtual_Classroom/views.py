from django.shortcuts import render, redirect, HttpResponse
from Vclass.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Vclass.models import CustomUser


def BASE(request):
    return render(request, 'base.html')


def LOGIN(request):
    return render(request, 'login.html')


def doLogin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password'), )
        if user != None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('admins_home')
            elif user_type == '2':
                return redirect('teacher_home')
            elif user_type == '3':
                return redirect('student_home')
            else:
                messages.error(request, 'Invalid Email or Password!')
                return redirect('login')
        else:
            messages.error(request, 'Invalid Email or Password!')
            return redirect('login')

    return render(request, 'login.html')


def doLogout(request):
    logout(request)
    return redirect('login')


def PROFILE(request):
    user = CustomUser.objects.get(id=request.user.id)

    context = {
        "user": user,
    }
    return render(request, 'profile.html', context)


def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        #username = request.POST.get('username')
        #email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id = request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name

            if password !=None and password != "":
                customuser.set_password(password)
            customuser.save()
            messages.success(request,'Profile updated successfully')
        except:
            messages.error(request,'Failed to update profile')

    return render(request,'profile.html')

