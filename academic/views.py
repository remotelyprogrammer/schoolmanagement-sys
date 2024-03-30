from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import GradeLevel, SchoolYear, Subject
from .forms import SchoolYearForm, GradeLevelForm, SubjectForm


def index(request):
    return HttpResponse("Hello, world. You're at the academic index.")


class SchoolYearCreateView(CreateView):
	model = SchoolYear
	template_name = 'academic/school-year-create.html'
	form_class = SchoolYearForm


class GradeLevelCreateView(CreateView):
	model = GradeLevel
	template_name = 'academic/grade-level-create.html'
	form_class = GradeLevelForm


class SubjectCreateView(CreateView):
	model = Subject
	template_name = 'academic/subject-create.html'
	form_class = SubjectForm