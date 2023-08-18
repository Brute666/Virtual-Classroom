from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import CourseForm


def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')  # Redirect to a course list view
    else:
        form = CourseForm()

    context = {'form': form}
    return render(request, 'add_course.html', context)