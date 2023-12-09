from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin

from ccam.academics.filters import CommitteeFilterSet, KnowledgeCertificateGradesFilterSet
from ccam.academics.models import Committee, KnowledgeCGrades, Subject
from ccam.core.views import FilteredListView
from ccam.people.mixins import UserIsTeacherTestMixin
from ccam.people.teachers.models import Teacher


class TeacherCommitteesListView(LoginRequiredMixin, UserIsTeacherTestMixin, FilteredListView):
    model = Committee
    template_name = "academics/teachers/teacher_committees_filter.html"
    filterset_class = CommitteeFilterSet
    paginate_by = settings.PAGINATE_BY
    teacher = None

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        teacher_pk = kwargs.get("pk")
        self.teacher = Teacher.objects.get(pk=teacher_pk)

    def get_queryset(self):
        return Committee.objects.filter(teachers__in=[self.teacher])


class KnowledgeCertificateGradesListView(LoginRequiredMixin, UserIsTeacherTestMixin, FilteredListView):
    model = KnowledgeCGrades
    template_name = "academics/teachers/knowledge_certificate_assessments.html"
    filterset_class = KnowledgeCertificateGradesFilterSet
    paginate_by = settings.PAGINATE_BY
    committee_subject = None

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        subject_id = kwargs.get("pk")
        self.committee_subject = Subject.objects.get(id=subject_id)

    def get_queryset(self):
        return KnowledgeCGrades.objects.filter(subject__id=self.committee_subject.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subject_name"] = self.committee_subject.name
        return context
