from django.urls import path
from . import views

app_name = 'academic'

urlpatterns = [
    path("", views.index, name="index"),
    path("school-year-create", views.SchoolYearCreateView.as_view(), name="school-year-create"),
    path("grade-level-create", views.GradeLevelCreateView.as_view(), name="grade-level-create"),
    path("subject-create", views.SubjectCreateView.as_view(), name="subject-create"),
    path("section-create", views.SectionCreateView.as_view(), name="section-create"),
    path("curriculum-create", views.CurriculumCreateView.as_view(), name="curriculum-create"),
]