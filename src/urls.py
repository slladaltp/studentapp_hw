"""django_students URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from homework.views import IndexView, StudentListView, StudentListUpdate, StudentListDelete, \
    StudentListAdd, StudentListDetail, base_template, get_reset_password, get_welcome_email, get_email_verification, \
    SendMailPage, CourseListAdd, CourseListDelete, CourseListUpdate, CourseListDetail, CourseListView, \
    TeacherListAdd, TeacherListDelete, TeacherListUpdate, TeacherListDetail, TeacherListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', IndexView.as_view()),
    path('base/', base_template),
    path('send_mail/', SendMailPage.as_view()),
    path('reset_password/', get_reset_password),
    path('welcome_email/', get_welcome_email),
    path('email_verification/', get_email_verification),
    path('list_student/', StudentListView.as_view(), name='list_student'),
    path('info_student/<int:pk>', StudentListDetail.as_view(), name='info_student'),
    path('update_student/<int:pk>', StudentListUpdate.as_view(), name='update_student'),
    path('delete_student/<int:pk>', StudentListDelete.as_view(), name='delete_student'),
    path('add_student/', StudentListAdd.as_view(), name='add_student'),
    path('list_course/', CourseListView.as_view(), name='list_course'),
    path('info_course/<int:pk>', CourseListDetail.as_view(), name='info_course'),
    path('update_course/<int:pk>', CourseListUpdate.as_view(), name='update_course'),
    path('delete_course/<int:pk>', CourseListDelete.as_view(), name='delete_course'),
    path('add_course/', CourseListAdd.as_view(), name='add_course'),
    path('list_teacher/', TeacherListView.as_view(), name='list_teacher'),
    path('info_teacher/<int:pk>', TeacherListDetail.as_view(), name='info_teacher'),
    path('update_teacher/<int:pk>', TeacherListUpdate.as_view(), name='update_teacher'),
    path('delete_teacher/<int:pk>', TeacherListDelete.as_view(), name='delete_teacher'),
    path('add_teacher/', TeacherListAdd.as_view(), name='add_teacher')
]
