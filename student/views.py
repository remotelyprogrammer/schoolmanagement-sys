from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Student, Address, Contact
from .forms import StudentForm, AddressForm, ContactForm
from django.views import View


from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the student index.")


class CreateStudentView(View):
    template_name = 'student/student-create.html'

    def get(self, request, *args, **kwargs):
        form = StudentForm()
        address_form = AddressForm()
        contact_form = ContactForm()
        return render(request, self.template_name, {
            'form': form,
            'address_form': address_form,
            'contact_form': contact_form,
        })

    def post(self, request, *args, **kwargs):
        form = StudentForm(request.POST)
        address_form = AddressForm(request.POST)
        contact_form = ContactForm(request.POST)

        if form.is_valid() and address_form.is_valid() and contact_form.is_valid():
            student = form.save()
            address = address_form.save(commit=False)
            address.student = student
            address.save()
            contact = contact_form.save(commit=False)
            contact.student = student
            contact.save()

            return redirect('student:index')  # Adjust the redirect to where you need.
        
        return render(request, self.template_name, {
            'form': form,
            'address_formset': address_form,
            'contact_formset': contact_form,
        })