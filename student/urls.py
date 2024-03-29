from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.StudentCreateView.as_view(), name="student-create"),
]