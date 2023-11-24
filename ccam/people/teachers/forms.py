from betterforms.multiform import MultiModelForm
from django import forms
from django.urls import reverse_lazy

from ccam.academics.models import Course
from ccam.people.forms import PersonForm

from .models import Teacher


class TeacherForm(forms.ModelForm):
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        widget=forms.Select(
            attrs={
                "hx-trigger": "change",
                "hx-get": reverse_lazy("academics:course_subjects"),
                "hx-target": "#id_teacher-subjects",
                "hx-swap": "innerHTML",
            }
        ),
    )

    class Meta:
        model = Teacher
        fields = ("subjects", "course")


class TeacherPersonMultiForm(MultiModelForm):
    form_classes = {"person": PersonForm, "teacher": TeacherForm}
