from django.views.generic import TemplateView


class KnowledgeCertificateCreateView(TemplateView):
    template_name = "academics/knowledge_certificate_form.html"


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


class CoordinatorsAddCourse(TemplateView):
    template_name = "academics/coordinators_academics/add_course.html"


class CoordinatorsSubjectList(TemplateView):
    template_name = "academics/coordinators_academics/subjects_list.html"


class AddCourseView(TemplateView):
    template_name = "academics/coordinators_academics/add_course.html"


class SubjectListView(TemplateView):
    template_name = "academics/teacher_academics/subject_list.html"


class SubjectCourseProgressListView(TemplateView):
    template_name = "academics/teacher_academics/subject_course_progress_list.html"


class SubjectKnowledgeCertificateAssessView(TemplateView):
    template_name = "academics/teacher_academics/knowledge_certificate_assessment.html"


class SubjectCourseProgressAssessView(TemplateView):
    template_name = "academics/teacher_academics/course_progress_assessments.html"


class TrackProcessesListView(TemplateView):
    template_name = "academics/student_academics/processes_list.html"
