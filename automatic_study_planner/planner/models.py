from django.db import models

# Create your models here.


class StudyInfo(models.Model):
    no_of_subjects = models.CharField(max_length=50, db_column="subject")
    no_of_days = models.IntegerField(db_column="no_of_days")

    class Meta:
        db_table = "study_info"
        abstract = True


class SubjectInfo(models.Model):
    name = models.CharField(max_length=250,db_column="subject_name")
    difficulty_level = models.IntegerField(db_column="difficulty_level")
    no_of_chapters = models.IntegerField(db_column="no_of_chapters")
    form_id = models.ForeignKey(StudyInfo, null=False, db_column="form_id", on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "subject_info"
        abstract = True

