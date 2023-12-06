from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from ccam.academics.filters import SubjectFilterSet
from ccam.academics.forms import CommitteeForm, SubjectForm
from ccam.academics.models import Committee, Subject
from ccam.core.views import FilteredListView
from ccam.people.mixins import UserIsCourseCoordinatorTestMixin


class SubjectCreateView(LoginRequiredMixin, UserIsCourseCoordinatorTestMixin, SuccessMessageMixin, CreateView):
    model = Subject
    success_url = reverse_lazy("people:coordinators:home")
    success_message = _("Disciplina cadastrada com sucesso!")
    template_name = "academics/coordinators/subject_form.html"
    form_class = SubjectForm

    @transaction.atomic
    def form_valid(self, form):
        subject = form.save(commit=False)
        subject.created_by = self.request.user
        subject.updated_by = self.request.user
        return super().form_valid(form)


class SubjectListView(LoginRequiredMixin, UserIsCourseCoordinatorTestMixin, FilteredListView):
    model = Subject
    filterset_class = SubjectFilterSet
    template_name = "academics/coordinators/subject_list.html"
    paginate_by = settings.PAGINATE_BY


class SubjectUpdateView(LoginRequiredMixin, UserIsCourseCoordinatorTestMixin, SuccessMessageMixin, UpdateView):
    model = Subject
    form_class = SubjectForm
    success_message = _("Disciplina atualizada com sucesso!")
    success_url = reverse_lazy("academics:subjects_list")
    template_name = "academics/coordinators/subject_form.html"


class SubjectDetailView(LoginRequiredMixin, DetailView):
    template_name = "academics/coordinators/subject_detail.html"
    model = Subject
    context_object_name = "subject"


class SubjectDeleteView(LoginRequiredMixin, UserIsCourseCoordinatorTestMixin, SuccessMessageMixin, DeleteView):
    model = Subject
    template_name = "academics/coordinators/subject_check_delete.html"
    success_url = reverse_lazy("academics:subjects_list")
    success_message = _("Disciplina deletada com sucesso!")


class SelectSubjectForCommitteeListView(LoginRequiredMixin, UserIsCourseCoordinatorTestMixin, FilteredListView):
    model = Subject
    template_name = "academics/coordinators/subject_for_committee_filter.html"
    filterset_class = SubjectFilterSet
    paginate_by = settings.PAGINATE_BY


class CommitteeCreateView(LoginRequiredMixin, UserIsCourseCoordinatorTestMixin, SuccessMessageMixin, CreateView):
    form_class = CommitteeForm
    model = Committee
    template_name = "academics/coordinators/committee_form.html"
    success_url = reverse_lazy("people:coordinators:home")
    success_message = _("Banca para disciplina criada com sucesso!")
