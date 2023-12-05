from typing import Any
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, DetailView, TemplateView, UpdateView

from ccam.academics.filters import KnowledgeCertificateFilterSet, SubjectFilterSet, SubjectDispensalFilterSet
from ccam.academics.forms import KnowledgeCertificateForm, SubjectForm
from ccam.academics.models import Course, KnowledgeCertificate, Subject, SubjectDispensal, KnowledgeCGrades
from ccam.core.views import FilteredListView


class SubjectCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Subject
    success_url = reverse_lazy("people:coordinators:home")
    success_message = _("Disciplina cadastrada com sucesso!")
    template_name = "academics/coordinators/subject_form.html"
    form_class = SubjectForm

    @transaction.atomic
    def form_valid(self, form):
        subject = form.save(commit=False)
        subject.created_by = self.request.user
        subject.updated_by = self.request.user
        return super().form_valid(form)


class SubjectListView(LoginRequiredMixin, FilteredListView):
    model = Subject
    filterset_class = SubjectFilterSet
    template_name = "academics/coordinators/subject_list.html"
    paginate_by = settings.PAGINATE_BY


class SubjectUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Subject
    form_class = SubjectForm
    success_message = _("Disciplina atualizada com sucesso!")
    success_url = reverse_lazy("academics:subjects_list")
    template_name = "academics/coordinators/subject_form.html"


class SubjectDetailView(LoginRequiredMixin, DetailView):
    template_name = "academics/coordinators/subject_detail.html"
    model = Subject
    context_object_name = "subject"


class SubjectDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Subject
    template_name = "academics/coordinators/subject_check_delete.html"
    success_url = reverse_lazy("academics:subjects_list")
    success_message = _("Disciplina deletada com sucesso!")


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


class KnowledgeCertificateSubjectList(LoginRequiredMixin, FilteredListView):
    model = Subject
    filterset_class = SubjectFilterSet
    template_name = "academics/coordinators/subject_list.html"
    paginate_by = settings.PAGINATE_BY


class KnowledgeCertificateCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "academics/students/knowledge_certificate_form.html"
    form_class = KnowledgeCertificateForm
    success_url = reverse_lazy("people:students:home")
    success_message = _("Certificação de conhecimento solicitada com sucesso!")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["student"] = self.request.user.person.student_person
        return kwargs


class CourseProgressCreateView(TemplateView):
    template_name = "academics/course_progress_form.html"


class SeacKnowledgeCertificatesListView(LoginRequiredMixin, FilteredListView):
    model = KnowledgeCertificate
    filterset_class = KnowledgeCertificateFilterSet
    template_name = "academics/seac_academics/seac_view_knowledge_certificates.html"
    paginate_by = settings.PAGINATE_BY


class SeacSubjectDispensalListView(LoginRequiredMixin, FilteredListView):
    model = SubjectDispensal
    filterset_class = SubjectDispensalFilterSet
    template_name = "academics/seac_academics/seac_view_courses_dispensal.html"
    paginate_by = settings.PAGINATE_BY


class SeacKnowledgeCertificatesStudentDetails(LoginRequiredMixin, DetailView):
    model = KnowledgeCertificate
    template_name = "academics/seac_academics/knowledge_certificates_student_details.html"
    context_object_name = "knowledge_certificate"


class SeacCoursesDispensalStudentDetails(TemplateView):
    template_name = "academics/seac_academics/courses_dispensal_student_details.html"


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
