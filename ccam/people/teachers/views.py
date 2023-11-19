from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, TemplateView

from ccam.people.teachers.models import Teacher

from .forms import TeacherPersonMultiForm


class TeacherHomeView(TemplateView):
    template_name = "teachers/home.html"


class TeacherListView(TemplateView):
    template_name = "teachers/teachers_list.html"


class TeacherCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "teachers/teacher_form.html"
    model = Teacher
    form_class = TeacherPersonMultiForm
    success_message = _("Professor criado com sucesso!")
    success_url = reverse_lazy("people:managers:home")

    @transaction.atomic
    def form_valid(self, form):
        person = form["person"].save(commit=False)
        person.created_by = self.request.user
        person.updated_by = self.request.user
        teacher = form["teacher"].save(commit=False)
        teacher.created_by = self.request.user
        teacher.updated_by = self.request.user
        teacher.person = person
        return super().form_valid(form)


class TeacherDetailView(TemplateView):
    template_name = "teachers/teachers_detail.html"
