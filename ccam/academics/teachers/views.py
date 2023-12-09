from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin

from ccam.academics.filters import CommitteeFilterSet
from ccam.academics.models import Committee
from ccam.core.views import FilteredListView
from ccam.people.mixins import UserIsTeacherTestMixin


class TeacherCommitteesListView(LoginRequiredMixin, UserIsTeacherTestMixin, FilteredListView):
    model = Committee
    template_name = "academics/teachers/teacher_committees_filter.html"
    filterset_class = CommitteeFilterSet
    paginate_by = settings.PAGINATE_BY
