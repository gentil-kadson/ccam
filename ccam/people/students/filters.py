import django_filters
from django.utils.translation import gettext_lazy as _

from ccam.academics.models import Course
from ccam.people.filters import PersonFilterSet

from .models import Student


class StudentFilterSet(PersonFilterSet, django_filters.FilterSet):
    course = django_filters.ModelChoiceFilter(label=_("Curso"), queryset=Course.objects.all())

    class Meta:
        model = Student
        fields = {"current_grade_semester": ["exact"], "course": ["exact"]} | PersonFilterSet.Meta.fields
