from typing import Any
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView, UpdateView, FormView
from django.urls import reverse_lazy
from ccam.academics.forms import RejectStudentKnowledgeCertificateForm, RejectStudentSubjectDispensalForm
from ccam.academics.filters import KnowledgeCertificateFilterSet, SubjectFilterSet, SubjectDispensalFilterSet
from ccam.academics.models import Course, KnowledgeCertificate, Subject, SubjectDispensal, KnowledgeCGrades
from ccam.core.views import FilteredListView
from ccam.people.mixins import UserIsSeacEmployeeTestMixin


class CourseSubjects(TemplateView):
    template_name = "academics/_course_subjects.html"

    def get_course_id(self):
        course_id = self.request.GET.get("teacher-course")
        # If a blank option is selected, course_id comes as '' (falsy value)
        return course_id if course_id else 0

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course_id = self.get_course_id()
        course = Course.objects.filter(id=course_id)

        if course.exists():
            subjects = course.first().subjects.all()
        else:
            subjects = []
        context["course_subjects"] = subjects
        return context


class KnowledgeCertificateSubjectList(LoginRequiredMixin, UserIsSeacEmployeeTestMixin, FilteredListView):
    model = Subject
    filterset_class = SubjectFilterSet
    template_name = "academics/coordinators/subject_list.html"
    paginate_by = settings.PAGINATE_BY

class SeacKnowledgeCertificatesListView(LoginRequiredMixin, UserIsSeacEmployeeTestMixin, FilteredListView):
    model = KnowledgeCertificate
    filterset_class = KnowledgeCertificateFilterSet
    template_name = "academics/seac_academics/seac_view_knowledge_certificates.html"
    paginate_by = settings.PAGINATE_BY


class SeacSubjectDispensalListView(LoginRequiredMixin, UserIsSeacEmployeeTestMixin, FilteredListView):
    model = SubjectDispensal
    filterset_class = SubjectDispensalFilterSet
    template_name = "academics/seac_academics/seac_view_courses_dispensal.html"
    context_object_name = "subject_dispensal"
    paginate_by = settings.PAGINATE_BY


class SeacKnowledgeCertificateUpdateView(LoginRequiredMixin, UserIsSeacEmployeeTestMixin, UpdateView):
    model = KnowledgeCertificate
    fields = ("status", "justification")
    template_name = "academics/seac_academics/knowledge_certificates_student_details.html"
    context_object_name = "knowledge_certificate"
    success_url = reverse_lazy("academics:knowledge_certificates")
    

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["subjects"] = context["knowledge_certificate"].subjects.all()
        return context
    
class SeacCoursesDispensalUpdateView(LoginRequiredMixin, UserIsSeacEmployeeTestMixin, UpdateView):
    model = SubjectDispensal
    fields = ("status", "justification")
    template_name = "academics/seac_academics/courses_dispensal_student_details.html"
    context_object_name = "course_dispensal"
    success_url = reverse_lazy("academics:courses_dispensal")

class RejectStudentKnowledgeCertificateFormView(LoginRequiredMixin, UserIsSeacEmployeeTestMixin, UpdateView):
    model = KnowledgeCertificate
    template_name = "academics/seac_academics/rejected_kc_modal.html"
    form_class = RejectStudentKnowledgeCertificateForm
    success_url = reverse_lazy("people:seac:home")

class RejectStudentSubjectDispensalFormView(LoginRequiredMixin, UserIsSeacEmployeeTestMixin, UpdateView):
    model = SubjectDispensal
    template_name = "academics/seac_academics/rejected_cd_modal.html"
    form_class = RejectStudentSubjectDispensalForm
    success_url = reverse_lazy("people:seac:home")

class CoordinatorsCommittee(TemplateView):
    template_name = "academics/coordinators_academics/committee.html"


class CoordinatorsCourseProgressComittee(TemplateView):
    template_name = "academics/coordinators_academics/course_progress_committee.html"


class CoordinatorsSubjectList(TemplateView):
    template_name = "academics/coordinators_academics/subjects_list.html"


class CoordinatorsCourseProgressSubjectList(TemplateView):
    template_name = "academics/coordinators_academics/course_progress_subject_list.html"


class SubjectCourseProgressListView(TemplateView):
    template_name = "academics/teacher_academics/subject_course_progress_list.html"


class SubjectKnowledgeCertificateAssessView(TemplateView):
    template_name = "academics/teacher_academics/knowledge_certificate_assessment.html"


class SubjectCourseProgressAssessView(TemplateView):
    template_name = "academics/teacher_academics/course_progress_assessments.html"


class TrackProcessesListView(TemplateView):
    template_name = "academics/student_academics/processes_list.html"
