from rest_framework import serializers
from automatic_study_planner.planner.models import StudentInfo, SubjectInfo, TimeTableGenerated


class StudentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfo
        fields = "__all__"


class SubjectInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectInfo
        fields = "__all__"


class TimeTableGeneratedSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTableGenerated
        fields = "__all__"
