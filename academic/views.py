from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import GradeLevel, SchoolYear, Subject, Section
from .forms import SchoolYearForm, GradeLevelForm, SubjectForm, SectionForm
from django.urls import reverse_lazy


def index(request):
    return HttpResponse("Hello, world. You're at the academic index.")


class SchoolYearCreateView(CreateView):
	model = SchoolYear
	template_name = 'academic/school-year-create.html'
	form_class = SchoolYearForm
	success_url = reverse_lazy('academic:index')


class GradeLevelCreateView(CreateView):
	model = GradeLevel
	template_name = 'academic/grade-level-create.html'
	form_class = GradeLevelForm
	success_url = reverse_lazy('academic:index')


class SubjectCreateView(CreateView):
	model = Subject
	template_name = 'academic/subject-create.html'
	form_class = SubjectForm
	success_url = reverse_lazy('academic:index')


class SectionCreateView(CreateView):
	model = Section
	template_name = 'academic/section-create.html'
	form_class = SectionForm
	success_url = reverse_lazy('academic:index')