from django import forms

from ccam.academics.models import KnowledgeCertificate, Subject


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ("name", "course", "grade_semester_availability", "educational_level")


class KnowledgeCertificateForm(forms.ModelForm):
    class Meta:
        model = KnowledgeCertificate
        fields = ("subjects",)
        widgets = {"subjects": forms.widgets.CheckboxSelectMultiple()}

    def __init__(self, *args, **kwargs):
        student = kwargs.pop("student")
        super().__init__(*args, **kwargs)
        self.fields["subjects"].queryset = Subject.objects.filter(
            grade_semester_availability=student.current_grade_semester, course=student.course
        )
