from django.shortcuts import render
from .models import Enrollment
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import EnrollmentForm

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the enrollment index.")


class CreateEnrollmentView(CreateView):
    model = Enrollment
    template_name = 'enrollment/create-enrollment.html'
    form_class = EnrollmentForm
    success_url = reverse_lazy('enrollment:index')  # Adjust this to where you want to redirect after success

    def form_valid(self, form):
        # Check if the student is already enrolled in the selected school year
        student = form.cleaned_data['student']
        school_year = form.cleaned_data['school_year']
        enrollment_exists = Enrollment.objects.filter(student=student, school_year=school_year).exists()

        if enrollment_exists:
            # If the student is already enrolled in this school year, show an error message
            form.add_error(None, 'This student is already enrolled in the selected school year.')
            return self.form_invalid(form)

        # If the check passes, proceed with the normal form handling, which saves the Enrollment
        return super().form_valid(form)

    def form_invalid(self, form):
        # If the form is invalid, return to the same page with error messages
        return self.render_to_response(self.get_context_data(form=form))