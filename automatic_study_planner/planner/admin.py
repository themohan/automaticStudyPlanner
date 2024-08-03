from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(StudentInfo)
class StudentInfoAdmin(admin.ModelAdmin):
    pass

@admin.register(SubjectInfo)
class SubjectInfoAdmin(admin.ModelAdmin):
    pass

@admin.register(TimeTableGenerated)
class TimeTableGeneratedAdmin(admin.ModelAdmin):
    pass