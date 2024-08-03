from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class StudentInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    no_of_subjects = models.CharField(max_length=255, null=False)
    no_of_days = models.IntegerField(null=False)
    no_of_hours = models.IntegerField(null=False)
    progress = models.IntegerField(default=0)


class SubjectInfo(models.Model):
    name = models.CharField(max_length=255)
    difficulty_level = models.IntegerField()
    no_of_chapters = models.IntegerField()
    student_info_id = models.ForeignKey(StudentInfo, null=False, db_column="form_id", on_delete=models.PROTECT)


class TimeTableGenerated(models.Model):
    day = models.IntegerField()
    subjects = models.CharField(max_length=500)
    chapters = models.CharField(max_length=255)
    student_info_id = models.ForeignKey(StudentInfo, null=False, db_column="form_id", on_delete=models.PROTECT)
