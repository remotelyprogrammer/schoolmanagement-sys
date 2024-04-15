from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import GradeLevel, SchoolYear, Subject, Section, Curriculum, Shift, Department
from .forms import SchoolYearForm, GradeLevelForm, SubjectForm, SectionForm, CurriculumForm, DepartmentForm, ShiftForm
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


class CurriculumCreateView(CreateView):
	model = Curriculum
	template_name = 'academic/curriculum-create.html'
	form_class = CurriculumForm
	success_url = reverse_lazy('academic:index')


class DepartmentCreateView(CreateView):
	model = Department
	template_name = 'academic/department-create.html'
	form_class = DepartmentForm
	success_url = reverse_lazy('academic:index')


class ShiftCreateView(CreateView):
	model = Shift
	template_name = 'academic/shift-create.html'
	form_class = ShiftForm
	success_url = reverse_lazy('academic:index')