from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from ccam.academics.filters import SubjectFilterSet
from ccam.academics.models import Course, Subject
from ccam.core.views import FilteredListView


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


class CourseProgressCreateView(TemplateView):
    template_name = "academics/course_progress_form.html"


class SeacViewKnowledgeCertificates(TemplateView):
    template_name = "academics/seac_academics/seac_view_knowledge_certificates.html"


class SeacViewCoursesDispensal(TemplateView):
    template_name = "academics/seac_academics/seac_view_courses_dispensal.html"


class SeacKnowledgeCertificatesStudentDetails(TemplateView):
    template_name = "academics/seac_academics/knowledge_certificates_student_details.html"


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
