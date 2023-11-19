from ccam.people.coordinators.models import Coordinator
from ccam.academics.models import Course
from django import forms
from betterforms.multiform import MultiModelForm
from ccam.people.forms import PersonForm


class CoordinatorsForm(forms.ModelForm):
    course = forms.ModelChoiceField(Course.objects.all())

    class Meta:
        model = Coordinator
        fields = ("course",)

    def save(self, commit=True):
        instance = super().save(commit)
        instance.course = self.cleaned_data["course"]
        if commit:
            instance.save()
            self.cleaned_data["course"].coordinator = instance
            self.cleaned_data["course"].save()
        return instance


class CoordinatorsMultiForm(MultiModelForm):
    form_classes = {"person": PersonForm, "coordinator": CoordinatorsForm}
