from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, TemplateView

from ccam.people.teachers.models import Teacher

from .forms import TeacherPersonMultiForm


class TeacherHomeView(TemplateView):
    template_name = "teachers/home.html"


class TeacherListView(TemplateView):
    template_name = "teachers/teachers_list.html"


class TeacherCreateView(LoginRequiredMixin, CreateView, SuccessMessageMixin):
    template_name = "teachers/teacher_form.html"
    model = Teacher
    form_class = TeacherPersonMultiForm
    success_message = _("Professor criado com sucesso!")
    success_url = reverse_lazy("people:managers:home")


class TeacherDetailView(TemplateView):
    template_name = "teachers/teachers_detail.html"
