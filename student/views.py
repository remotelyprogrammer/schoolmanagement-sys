from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from .models import PersonalInfo

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class StudentCreateView(CreateView):
	model = PersonalInfo
	template_name = 'student/student-create.html'
	fields = ('__all__')