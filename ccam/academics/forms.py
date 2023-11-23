from django import forms

from ccam.academics.models import Subject


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ("name", "course", "grade_semester_availability", "educational_level")
