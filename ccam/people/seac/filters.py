import django_filters

from ccam.people.filters import PersonFilterSet

from .models import SEACStaff


class SEACStaffFilterSet(PersonFilterSet, django_filters.FilterSet):
    class Meta:
        model = SEACStaff
        fields = {"role": ["exact"]} | PersonFilterSet.Meta.fields
