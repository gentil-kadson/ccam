from django.views.generic import TemplateView
from typing import Any
from django.views.generic import TemplateView, CreateView, DetailView
from django.db import models, transaction
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from ccam.people.students.forms import StudentsMultiForm
from ccam.people.students.models import Student


class StudentHomeView(TemplateView):
    template_name = "students/home.html"


class StudentListView(TemplateView):
    template_name = "students/students_list.html"


class StudentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "students/students_form.html"
    form_class = StudentsMultiForm
    model = Student
    success_url = reverse_lazy("people:managers:home")
    success_message = _("Estudante criado com sucesso!")

    @transaction.atomic
    def form_valid(self, form):
        person = form["person"].save(commit=False)
        person.created_by = self.request.user
        person.updated_by = self.request.user
        student = form["student"].save(commit=False)
        student.person = person
        student.created_by = self.request.user
        student.updated_by = self.request.user
        return super().form_valid(form)


class StudentDetailView(TemplateView):
    template_name = "students/students_detail.html"
