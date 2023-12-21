from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import UpdateView

from ccam.academics.filters import KnowledgeCertificateFilterSet, SubjectDispensalFilterSet
from ccam.academics.forms import RejectStudentKnowledgeCertificateForm, RejectStudentSubjectDispensalForm
from ccam.academics.models import KnowledgeCertificate, SubjectDispensal
from ccam.core.views import FilteredListView
from ccam.people.mixins import UserIsSeacEmployeeTestMixin


class SeacKnowledgeCertificatesListView(LoginRequiredMixin, UserIsSeacEmployeeTestMixin, FilteredListView):
    model = KnowledgeCertificate
    filterset_class = KnowledgeCertificateFilterSet
    template_name = "academics/seac_academics/seac_view_knowledge_certificates.html"
    paginate_by = settings.PAGINATE_BY


class SeacSubjectDispensalListView(LoginRequiredMixin, UserIsSeacEmployeeTestMixin, FilteredListView):
    model = SubjectDispensal
    filterset_class = SubjectDispensalFilterSet
    template_name = "academics/seac_academics/seac_view_courses_dispensal.html"
    context_object_name = "subject_dispensal"
    paginate_by = settings.PAGINATE_BY


class SeacKnowledgeCertificateUpdateView(
    LoginRequiredMixin, UserIsSeacEmployeeTestMixin, SuccessMessageMixin, UpdateView
):
    model = KnowledgeCertificate
    fields = ("status", "justification")
    template_name = "academics/seac_academics/knowledge_certificates_student_details.html"
    context_object_name = "knowledge_certificate"
    success_message = _("Solicitação atualizada com sucesso")
    success_url = reverse_lazy("academics:knowledge_certificates")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subjects"] = context["knowledge_certificate"].subjects.all()
        return context


class SeacCoursesDispensalUpdateView(LoginRequiredMixin, UserIsSeacEmployeeTestMixin, SuccessMessageMixin, UpdateView):
    model = SubjectDispensal
    fields = ("status", "justification")
    template_name = "academics/seac_academics/courses_dispensal_student_details.html"
    context_object_name = "course_dispensal"
    success_message = _("Solicitação atualizada com sucesso")
    success_url = reverse_lazy("academics:courses_dispensal")


class RejectStudentKnowledgeCertificateFormView(LoginRequiredMixin, UserIsSeacEmployeeTestMixin, UpdateView):
    model = KnowledgeCertificate
    template_name = "academics/seac_academics/rejected_kc_modal.html"
    form_class = RejectStudentKnowledgeCertificateForm
    success_url = reverse_lazy("people:seac:home")


class RejectStudentSubjectDispensalFormView(LoginRequiredMixin, UserIsSeacEmployeeTestMixin, UpdateView):
    model = SubjectDispensal
    template_name = "academics/seac_academics/rejected_cd_modal.html"
    form_class = RejectStudentSubjectDispensalForm
    success_url = reverse_lazy("people:seac:home")
