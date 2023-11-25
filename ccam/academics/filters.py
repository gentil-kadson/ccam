import django_filters

from .models import Course, Subject


class SubjectFilterSet(django_filters.FilterSet):
    course = django_filters.ModelChoiceFilter(queryset=Course.objects.all())

    class Meta:
        model = Subject
        fields = ("course", "name", "grade_semester_availability", "educational_level")
