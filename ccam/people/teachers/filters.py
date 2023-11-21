import django_filters

from ccam.people.filters import PersonFilterSet

from .models import Teacher


class TeacherFilterSet(PersonFilterSet, django_filters.FilterSet):
    class Meta:
        model = Teacher
        fields = {"subjects": ["exact"]} | PersonFilterSet.Meta.fields
