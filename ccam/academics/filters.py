import django_filters
from django.utils.translation import gettext_lazy as _

from ccam.core.models import EducationalLevel

from .models import Committee, Course, KnowledgeCertificate, Subject, SubjectDispensal


class SubjectFilterSet(django_filters.FilterSet):
    course = django_filters.ModelChoiceFilter(queryset=Course.objects.all())
    educational_level = django_filters.ChoiceFilter(empty_label=_("Todos"), choices=EducationalLevel.choices)
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Subject
        fields = ("course", "name", "grade_semester_availability", "educational_level")


class KnowledgeCertificateFilterSet(django_filters.FilterSet):
    class Meta:
        model = KnowledgeCertificate
        fields = ("status",)


class SubjectDispensalFilterSet(django_filters.FilterSet):
    class Meta:
        model = SubjectDispensal
        fields = ("status",)


class CommitteeFilterSet(django_filters.FilterSet):
    teacher_registration = django_filters.CharFilter(
        field_name="teachers__person__registration", lookup_expr="icontains", label="Matrícula do professor"
    )

    class Meta:
        model = Committee
        fields = ("subject",)
