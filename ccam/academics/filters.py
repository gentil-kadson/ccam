import django_filters
from django.utils.translation import gettext_lazy as _

from ccam.core.models import EducationalLevel

from .models import Committee, Course, KnowledgeCertificate, KnowledgeCGrades, Subject, SubjectDispensal


class SubjectFilterSet(django_filters.FilterSet):
    course = django_filters.ModelChoiceFilter(queryset=Course.objects.all())
    educational_level = django_filters.ChoiceFilter(empty_label=_("Todos"), choices=EducationalLevel.choices)
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains", label="Nome da disciplina")

    class Meta:
        model = Subject
        fields = ("course", "name", "grade_semester_availability", "educational_level")


class KnowledgeCertificateFilterSet(django_filters.FilterSet):
    class Meta:
        model = KnowledgeCertificate
        fields = ("student", "status",)


class KnowledgeCertificateGradesFilterSet(django_filters.FilterSet):
    student = django_filters.CharFilter(
        field_name="knowledge_certificate__student__person__name", lookup_expr="icontains", label=_("Nome do discente")
    )
    registration = django_filters.CharFilter(
        field_name="knowledge_certificate__student__person__registration",
        lookup_expr="icontains",
        label=_("Matrícula do discente"),
    )

    class Meta:
        model = KnowledgeCGrades
        exclude = ("student", "knowledge_certificate", "grade")

class SubjectDispensalGradesFilterSet(django_filters.FilterSet):
    student = django_filters.CharFilter(
        field_name="subject_dispensal__student__person__name", lookup_expr="icontains",
        label=_("Nome do discente")
    )
    registration = django_filters.CharFilter(
        field_name="subject_dispensal__student__person__registration",
        lookup_expr="icontains",
        label=_("Matrícula do discente")
    )

    class Meta:
        model = KnowledgeCGrades
        exclude = ("student", "subject_dispensal", "grade")

class SubjectDispensalFilterSet(django_filters.FilterSet):
    class Meta:
        model = SubjectDispensal
        fields = ("status", "student")


class CommitteeFilterSet(django_filters.FilterSet):
    teacher_registration = django_filters.CharFilter(
        field_name="teachers__person__registration", lookup_expr="icontains", label=_("Matrícula do professor")
    )

    class Meta:
        model = Committee
        fields = ("subject",)
