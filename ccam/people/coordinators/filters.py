import django_filters

from ccam.people.filters import PersonFilterSet

from .models import Coordinator


class CoordinatorsFilterSet(PersonFilterSet, django_filters.FilterSet):
    class Meta:
        model = Coordinator
        fields = {"course": ["exact"]} | PersonFilterSet.Meta.fields
