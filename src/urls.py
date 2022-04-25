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
from homework.views import index, index_with_get, students_json, \
    person_add, person_list, person_delete, person_update, group_add, \
    group_list, group_delete, group_update, subject_add, subject_list, subject_delete, \
    subject_update, course_add, course_list, course_delete, course_update, lesson_add, \
    lesson_list, lesson_delete, lesson_update, reset_password, email_verification, welcome_email

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('students_page/', index_with_get),
    path('students_json/', students_json),
    path('person/add', person_add),
    path('person/list', person_list),
    path('person/delete', person_delete),
    path('person/update', person_update),
    path('group/add', group_add),
    path('group/list', group_list),
    path('group/delete', group_delete),
    path('group/update', group_update),
    path('subject/add', subject_add),
    path('subject/list', subject_list),
    path('subject/delete', subject_delete),
    path('subject/update', subject_update),
    path('course/add', course_add),
    path('course/list', course_list),
    path('course/delete', course_delete),
    path('course/update', course_update),
    path('lesson/add', lesson_add),
    path('lesson/list', lesson_list),
    path('lesson/delete', lesson_delete),
    path('lesson/update', lesson_update),
    path('welcome_email', welcome_email),
    path('reset_password', reset_password),
    path('email_verification', email_verification)
]
