from ccam.people.students.models import Student
from django import forms
from betterforms.multiform import MultiModelForm
from ccam.people.forms import PersonForm


class StudentsForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("current_grade_semester", "course")


class StudentsMultiForm(MultiModelForm):
    form_classes = {"person": PersonForm, "student": StudentsForm}
