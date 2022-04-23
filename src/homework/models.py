from django.db.models import Model, CharField, DateTimeField, IntegerField
from django import forms

# Create your models here.


class DateTimeMixin(Model):
    created_at = DateTimeField(auto_now_add=True, null=True)
    updated_ad = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Student(DateTimeMixin, Model):

    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)


class Person(DateTimeMixin, Model):

    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    age_person = IntegerField(default='0')
    type_person = CharField(max_length=50)
    status_person = CharField(max_length=50, default='Active')


class Group(DateTimeMixin, Model):

    group_name = CharField(max_length=50)
    group_city = CharField(max_length=50)
    group_amount = IntegerField(default='0')
    group_type = CharField(max_length=50, default='Offline')


class Subject(DateTimeMixin, Model):

    subject_name = CharField(max_length=50)
    subject_level = CharField(max_length=50, default='Novice')


class Course(DateTimeMixin, Model):

    course_name = CharField(max_length=50)
    course_type = CharField(max_length=50, default='Offline')


class Lesson(DateTimeMixin, Model):

    lesson_name = CharField(max_length=50)
    lesson_type = CharField(max_length=50, default='Practice')

class EmailForms(forms.Form):
    """Форма для получения почты! """

    email = forms.EmailField(max_length=85)
