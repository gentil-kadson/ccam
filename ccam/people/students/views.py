from typing import Any

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, DetailView, TemplateView, UpdateView
from django_filters.views import FilterView

from ccam.people.students.filters import StudentFilterSet
from ccam.people.students.forms import StudentsMultiForm
from ccam.people.students.models import Student


class StudentHomeView(TemplateView):
    template_name = "students/home.html"


class StudentListView(LoginRequiredMixin, FilterView):
    model = Student
    filterset_class = StudentFilterSet
    template_name = "students/students_list.html"
    paginate_by = settings.PAGINATE_BY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_page = int(self.request.GET.get("page", 1))
        context.update({"current_page": current_page})
        return context


class StudentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "students/students_form.html"
    form_class = StudentsMultiForm
    model = Student
    success_url = reverse_lazy("people:students:list")
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


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy("list")


class StudentDetailView(DetailView):
    model = Student
    template_name = "students/students_detail.html"
    context_object_name = "student"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)


class StudentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Student
    form_class = StudentsMultiForm
    template_name = "students/students_form.html"
    success_url = reverse_lazy("people:students:list")
    success_message = _("Aluno editado com sucesso!")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(instance={"person": self.object.person, "student": self.object})
        return kwargs
