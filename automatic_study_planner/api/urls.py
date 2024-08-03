from django.urls import path
from . import views
from .views import create_study_form

urlpatterns = [

    path('create-study-info', create_study_form(), name="create-study-info"),

]
