from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.db import transaction
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from ccam.academics.filters import CommitteeFilterSet, SubjectFilterSet
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


class CommitteeCreateView(LoginRequiredMixin, UserIsCourseCoordinatorTestMixin, SuccessMessageMixin, CreateView):
    model = Committee
    form_class = CommitteeForm
    template_name = "academics/coordinators/committee_form.html"
    success_message = _(
        "Banca criada com sucesso! Você pode adicionar os professores que irão compô-la na página de listagem"
    )
    success_url = reverse_lazy("people:coordinators:home")
    paginate_courses_by = settings.PAGINATE_BY

    def get_course_subjects_filterset(self):
        coordinator_course = self.request.user.person.coordinator_person.course
        course_subjects = Subject.objects.filter(course=coordinator_course, committee_subject=None)
        return SubjectFilterSet(data=self.request.GET, queryset=course_subjects)

    def get_paginated_subjects(self):
        filtered_courses_queryset = self.get_course_subjects_filterset().qs
        return Paginator(object_list=filtered_courses_queryset, per_page=self.paginate_courses_by)

    def get_current_subjects_page(self):
        currnet_page = self.request.GET.get("page", 1)
        paginator = self.get_paginated_subjects()
        return paginator.page(currnet_page)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = self.get_course_subjects_filterset()
        context["paginator"] = self.get_paginated_subjects()
        context["current_page"] = self.get_current_subjects_page().number
        context["page_obj"] = self.get_current_subjects_page()
        context["object_list"] = context["paginator"].object_list
        return context

    @transaction.atomic
    def form_valid(self, form):
        committee = form.save(commit=False)
        committee.created_by = self.request.user
        committee.updated_by = self.request.user
        committee.coordinator = self.request.user.person.coordinator_person
        return super().form_valid(form)


class CommitteeListView(LoginRequiredMixin, UserIsCourseCoordinatorTestMixin, FilteredListView):
    model = Committee
    template_name = "academics/coordinators/committee_filter.html"
    filterset_class = CommitteeFilterSet
    paginate_by = settings.PAGINATE_BY


class CommitteeUpdateView(LoginRequiredMixin, UserIsCourseCoordinatorTestMixin, SuccessMessageMixin, DetailView):
    pass


class CommitteeDeleteView(LoginRequiredMixin, UserIsCourseCoordinatorTestMixin, SuccessMessageMixin, DeleteView):
    pass
