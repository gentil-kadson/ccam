from django import forms

from ccam.academics.models import Committee, KnowledgeCertificate, KnowledgeCGrades, Subject, SubjectDispensal, SubjectDGrades
from ccam.core.widgets import CCAMFileWidget


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ("name", "grade_semester_availability", "educational_level")


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

    def clean_teachers(self):
        current_teachers = self.instance.teachers.all()
        incoming_teacher = self.cleaned_data["teachers"]
        incoming_teacher_id = incoming_teacher[0].id
        if current_teachers.filter(id=incoming_teacher_id).exists():
            return current_teachers.exclude(id=incoming_teacher_id)
        return current_teachers.union(incoming_teacher)


class KnowledgeCertificateAssessmentForm(forms.ModelForm):
    class Meta:
        model = KnowledgeCGrades
        fields = ("grade",)

class SubjectDispensalAssessmentForm(forms.ModelForm):
    class Meta:
        model = SubjectDGrades
        fields = ("grade",)

class RejectStudentKnowledgeCertificateForm(forms.ModelForm):
    class Meta:
        model = KnowledgeCertificate
        fields = ("status", "justification")

class RejectStudentSubjectDispensalForm(forms.ModelForm):
    class Meta:
        model = SubjectDispensal
        fields = ("status", "justification")