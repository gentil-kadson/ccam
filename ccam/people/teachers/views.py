from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, DetailView, TemplateView, UpdateView

from ccam.academics.models import Course
from ccam.core.views import FilteredListView
from ccam.people.mixins import UserIsSeacCoordinatorTestMixin
from ccam.people.teachers.models import Teacher

from .filters import TeacherFilterSet
from .forms import TeacherPersonMultiForm


class TeacherHomeView(TemplateView):
    template_name = "teachers/home.html"


class TeacherListView(LoginRequiredMixin, UserIsSeacCoordinatorTestMixin, FilteredListView):
    model = Teacher
    filterset_class = TeacherFilterSet
    template_name = "teachers/teacher_filter.html"
    paginate_by = settings.PAGINATE_BY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"courses": Course.objects.all()})
        return context


class TeacherCreateView(LoginRequiredMixin, UserIsSeacCoordinatorTestMixin, SuccessMessageMixin, CreateView):
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


class TeacherDetailView(LoginRequiredMixin, UserIsSeacCoordinatorTestMixin, DetailView):
    model = Teacher
    template_name = "teachers/teacher_detail.html"
    context_object_name = "teacher"


class TeacherUpdateView(LoginRequiredMixin, UserIsSeacCoordinatorTestMixin, SuccessMessageMixin, UpdateView):
    model = Teacher
    form_class = TeacherPersonMultiForm
    template_name = "teachers/teacher_form.html"
    context_object_name = "teacher"
    success_message = _("Professor atualizado com sucesso")
    success_url = reverse_lazy("people:teachers:list")

    @transaction.atomic
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(instance={"person": self.object.person, "teacher": self.object})
        return kwargs


class TeacherDeleteView(LoginRequiredMixin, UserIsSeacCoordinatorTestMixin, SuccessMessageMixin, DeleteView):
    model = Teacher
    template_name = "teachers/teacher_check_delete.html"
    success_message = _("Professor removido com sucesso")
    success_url = reverse_lazy("people:teachers:list")
