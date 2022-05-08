from django.db.models import Model, CharField, DateTimeField, IntegerField, URLField, EmailField


class DateTimeMixin(Model):
    created_at = DateTimeField(auto_now_add=True, null=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Student(DateTimeMixin, Model):

    first_name = CharField(max_length=50,)
    last_name = CharField(max_length=50, default='Undefined')
    social_url = URLField(max_length=100)
    age = IntegerField(default='0')
    email = EmailField(max_length=100)


class Teacher(DateTimeMixin, Model):

    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    age = IntegerField(default='0')
    status = CharField(max_length=50, default='Active')


class Group(DateTimeMixin, Model):

    name = CharField(max_length=50)
    city = CharField(max_length=50)
    amount = IntegerField(default='0')
    type = CharField(max_length=50, default='Offline')


class Subject(DateTimeMixin, Model):

    name = CharField(max_length=50)
    level = CharField(max_length=50, default='Novice')


class Course(DateTimeMixin, Model):

    name = CharField(max_length=50)
    type = CharField(max_length=50, default='Offline')


class Lesson(DateTimeMixin, Model):

    name = CharField(max_length=50)
    type = CharField(max_length=50, default='Practice')
