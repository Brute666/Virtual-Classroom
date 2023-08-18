
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from .import views,admin_view,student_view,teacher_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE, name='base'),

    path('',views.LOGIN, name='login'), #login path
    path('doLogin', views.doLogin,name='doLogin'),
    path('doLogout',views.doLogout,name='logout'),

    #profile
    path('profile',views.PROFILE,name='profile'),
    path('profile/update',views.PROFILE_UPDATE,name='profile_update'),

    #admin panel
    path('admins/home',admin_view.HOME,name='admins_home'),
    path('admins/student/add',admin_view.ADD_STUDENT,name='add_student'),
    path('admins/student/view',admin_view.VIEW_STUDENT,name='view_student'),
    path('admins/student/edit', admin_view.EDIT_STUDENT, name='edit_student'),

    path('admins/course/add', admin_view.ADD_COURSE, name='add_course'),
    path('admins/course/view', admin_view.VIEW_COURSE, name='view_course'),
    path('admins/course/my', admin_view.MY_COURSE, name='my_course'),

    path('admins/teacher/add',admin_view.ADD_TEACHER,name='add_teacher'),
    path('admins/teacher/view', admin_view.VIEW_TEACHER, name='view_teacher'),

    #teacher panel
    path('teacher/home',teacher_view.HOME,name='teacher_home'),

    #student panel
    path('student/home',student_view.HOME,name='student_home'),


] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

