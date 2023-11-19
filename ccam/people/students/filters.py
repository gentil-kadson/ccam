import django_filters

from ccam.people.filters import PersonFilterSet

from .models import Student


class StudentFilterSet(PersonFilterSet, django_filters.FilterSet):
    class Meta:
        model = Student
        fields = {"current_grade_semester": ["exact"], "course": ["exact"]} | PersonFilterSet.Meta.fields
