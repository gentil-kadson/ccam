from betterforms.multiform import MultiModelForm
from django import forms

from ccam.people.forms import PersonForm

from .models import Teacher


class TeacherForm(forms.ModelForm):
    course = forms.ChoiceField()

    class Meta:
        model = Teacher
        fields = ("subjects", "course")


class TeacherPersonMultiForm(MultiModelForm):
    form_classes = {"person": PersonForm, "teacher": TeacherForm}
