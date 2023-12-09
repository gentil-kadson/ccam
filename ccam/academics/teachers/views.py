from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin

from ccam.academics.filters import CommitteeFilterSet
from ccam.academics.models import Committee
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
