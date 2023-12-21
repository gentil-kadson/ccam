from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DetailView

from ccam.academics.filters import KnowledgeCertificateFilterSet, SubjectDispensalFilterSet
from ccam.academics.forms import KnowledgeCertificateForm, SubjectDispensalForm
from ccam.academics.models import KnowledgeCertificate, SubjectDispensal
from ccam.core.mixins import UniqueConstraintErrorMessageMixin
from ccam.core.views import FilteredListView
from ccam.people.mixins import UserIsStudentTestMixin


class StudentAcademicsFormBaseMixin:
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["student"] = self.request.user.person.student_person
        return kwargs

    @transaction.atomic
    def form_valid(self, form):
        # Either an instance of KnowledgeCertificate or SubjectDispensal
        instance = form.save(commit=False)
        instance.student = self.request.user.person.student_person
        instance.created_by = self.request.user
        instance.updated_by = self.request.user
        return super().form_valid(form)


class SubjectDispensalCreateView(
    LoginRequiredMixin,
    UserIsStudentTestMixin,
    StudentAcademicsFormBaseMixin,
    UniqueConstraintErrorMessageMixin,
    SuccessMessageMixin,
    CreateView,
):
    template_name = "academics/students/subject_dispensal_form.html"
    model = SubjectDispensal
    form_class = SubjectDispensalForm
    success_message = _("Aproveitamento de Disciplina cadastrado com sucesso!")
    success_url = reverse_lazy("people:students:home")
    unique_constraint_error_msg = _("Você já possui uma solicitação pendente")


class SubjectDispensalListView(LoginRequiredMixin, UserIsStudentTestMixin, FilteredListView):
    template_name = "academics/students/subject_dispensal_filter.html"
    model = SubjectDispensal
    filterset_class = SubjectDispensalFilterSet
    paginate_by = settings.PAGINATE_BY

    def get_queryset(self):
        return SubjectDispensal.objects.filter(student=self.request.user.person.student_person)


class KnowledgeCertificateCreateView(
    LoginRequiredMixin,
    UserIsStudentTestMixin,
    StudentAcademicsFormBaseMixin,
    UniqueConstraintErrorMessageMixin,
    SuccessMessageMixin,
    CreateView,
):
    template_name = "academics/students/knowledge_certificate_form.html"
    form_class = KnowledgeCertificateForm
    success_url = reverse_lazy("people:students:home")
    success_message = _("Certificação de conhecimento solicitada com sucesso! Aguarde a avaliação")
    unique_constraint_error_msg = _("Você já possui uma solicitação em aberto")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["student"] = self.request.user.person.student_person
        return kwargs

    @transaction.atomic
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.student = self.request.user.person.student_person
        instance.created_by = self.request.user
        instance.updated_by = self.request.user
        return super().form_valid(form)


class KnowledgeCertificateListView(LoginRequiredMixin, UserIsStudentTestMixin, FilteredListView):
    template_name = "academics/students/knowledge_certificate_filter.html"
    model = KnowledgeCertificate
    paginate_by = settings.PAGINATE_BY
    filterset_class = KnowledgeCertificateFilterSet

    def get_queryset(self):
        return KnowledgeCertificate.objects.filter(student=self.request.user.person.student_person)


class SubjectDispensalApprovalCheckView(LoginRequiredMixin, UserIsStudentTestMixin, DetailView):
    model = SubjectDispensal
    template_name = "academics/students/_check_denial_justification.html"


class KnowledgeCertificateApprovalCheckView(LoginRequiredMixin, UserIsStudentTestMixin, DetailView):
    model = KnowledgeCertificate
    template_name = "academics/students/_check_denial_justification.html"
