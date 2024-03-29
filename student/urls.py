from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.CreateStudentView.as_view(), name="student-create"),
]