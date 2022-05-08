from django.contrib import admin
from django.utils.html import format_html

from homework.models import Student, Teacher, Group

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'age', 'email',)
    list_filter = ('age',)
    search_fields = ('first_name', 'last_name',)

    def full_name(self, instance):
        if instance.social_url:
            return format_html(f'<a href="{instance.social_url}"> {instance.first_name}{instance.last_name} </a>')
        else:
            return f'{instance.first_name}{instance.last_name}'

admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher)
admin.site.register(Group)
