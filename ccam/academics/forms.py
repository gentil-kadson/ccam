from django import forms

from ccam.academics.models import Committee, KnowledgeCertificate, Subject, SubjectDispensal
from ccam.core.widgets import CCAMFileWidget


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


class SubjectDispensalForm(forms.ModelForm):
    class Meta:
        model = SubjectDispensal
        fields = ("subjects", "previous_university_ppc", "previous_university_grades")
        widgets = {
            "previous_university_ppc": CCAMFileWidget(attrs={"label": "Histórico escolar da antiga universidade"}),
            "previous_university_grades": CCAMFileWidget(attrs={"label": "PPC da antiga universidade"}),
        }

    def __init__(self, *args, **kwargs):
        student = kwargs.pop("student")
        super().__init__(*args, **kwargs)
        self.fields["subjects"].queryset = Subject.objects.filter(
            grade_semester_availability=student.current_grade_semester, course=student.course
        )


class CommitteeForm(forms.ModelForm):
    class Meta:
        model = Committee
        fields = ("subject",)


class AddTeachersToCommitteeForm(forms.ModelForm):
    class Meta:
        model = Committee
        fields = ("teachers",)
