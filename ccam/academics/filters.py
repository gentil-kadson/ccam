import django_filters
from django.utils.translation import gettext_lazy as _

from ccam.core.models import EducationalLevel

from .models import Course, KnowledgeCertificate, Subject


class SubjectFilterSet(django_filters.FilterSet):
    course = django_filters.ModelChoiceFilter(queryset=Course.objects.all())
    educational_level = django_filters.ChoiceFilter(empty_label=_("Todos"), choices=EducationalLevel.choices)

    class Meta:
        model = Subject
        fields = ("course", "name", "grade_semester_availability", "educational_level")


class KnowledgeCertificateFilterSet(django_filters.FilterSet):
    class Meta:
        model = KnowledgeCertificate
        fields = ("student",)
