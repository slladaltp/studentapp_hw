from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, View
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from homework.forms import IndexForm, EmailSendForm
from homework.models import Student, Course, Teacher
from django.urls import reverse_lazy

from homework.send_email import send
# Create your views here.


class IndexView(View):

    def get(self, request):
        return render(request, 'index.html', {
            'form': IndexForm(),
        })

    def post(self, request):

        form = IndexForm(request.POST)
        if form.is_valid():
            student = Student()
            student.first_name = form.cleaned_data['first_name']

            student.save()

            return HttpResponse('Saved')

        return HttpResponse('Not Saved')


class StudentListView(ListView):

    model = Student
    template_name = 'student/list_student.html'


class StudentListDetail(DetailView):

    model = Student
    template_name = 'student/info_student.html'


class StudentListUpdate(UpdateView):

    model = Student
    fields = ['first_name', 'last_name']
    template_name = 'student/update_student.html'
    success_url = reverse_lazy('list_student')


class StudentListDelete(DeleteView):

    model = Student
    template_name = 'student/delete_student.html'
    success_url = reverse_lazy('list_student')


class StudentListAdd(CreateView):

    model = Student
    fields = ['first_name', 'last_name']
    template_name = 'student/add_student.html'
    success_url = reverse_lazy('list_student')


class CourseListView(ListView):

    model = Course
    template_name = 'course/list_course.html'


class CourseListDetail(DetailView):

    model = Course
    template_name = 'course/info_course.html'


class CourseListUpdate(UpdateView):

    model = Course
    fields = ['name']
    template_name = 'course/update_course.html'
    success_url = reverse_lazy('list_course')


class CourseListDelete(DeleteView):

    model = Course
    template_name = 'course/delete_course.html'
    success_url = reverse_lazy('list_course')


class CourseListAdd(CreateView):

    model = Course
    fields = ['name', 'type']
    template_name = 'course/add_course.html'
    success_url = reverse_lazy('list_course')


class TeacherListView(ListView):

    model = Teacher
    template_name = 'teacher/list_teacher.html'


class TeacherListDetail(DetailView):

    model = Teacher
    template_name = 'teacher/info_teacher.html'


class TeacherListUpdate(UpdateView):

    model = Teacher
    fields = ['first_name', 'last_name', 'age', 'status']
    template_name = 'teacher/update_teacher.html'
    success_url = reverse_lazy('list_teacher')


class TeacherListDelete(DeleteView):

    model = Teacher
    template_name = 'teacher/delete_teacher.html'
    success_url = reverse_lazy('list_teacher')


class TeacherListAdd(CreateView):

    model = Teacher
    fields = ['first_name', 'last_name', 'age', 'status']
    template_name = 'teacher/add_teacher.html'
    success_url = reverse_lazy('list_teacher')


def base_template(request):
    return render(request, 'base.html')


def get_reset_password(request):
    return render(request, 'email/reset_password.html')


def get_welcome_email(request):
    return render(request, 'email/welcome_email.html')


def get_email_verification(request):
    return render(request, 'email/email_verification.html')


class SendMailPage(View):

    def get(self, request):
        return render(request, 'email/send_mail.html', {
            'form': EmailSendForm(),
        })

    def post(self, request):
        form = EmailSendForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            to_email = form.cleaned_data['to_email']

            send(subject, to_email, 'email/mail_base.html', context={
                'message': message,
            }
                 )
            return HttpResponse('Was Sent')

        return HttpResponse('Error')
