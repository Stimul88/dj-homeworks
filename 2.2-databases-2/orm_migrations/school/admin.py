from django.contrib import admin

from .models import Student, Teacher, StudentTeacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


class StudentAInline(admin.TabularInline):
    model = StudentTeacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [StudentAInline]
