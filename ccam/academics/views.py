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


class CoordinatorsKnowledgeCertificateCommittees(TemplateView):
    template_name = "academics/coordinators_academics/knowledge_certificate_committees.html"


class CoordinatorsCoursesDispensalCommittees(TemplateView):
    template_name = "academics/coordinators_academics/courses_dispensal_committees.html"


class CoordinatorsAddCourse(TemplateView):
    template_name = "academics/coordinators_academics/add_course.html"


class CoordinatorsKCCoursesToAssembleCommittees(TemplateView):
    template_name = "academics/coordinators_academics/kc_courses_to_assemble_committee.html"


class CoordinatorsCDCoursesToAssembleCommittees(TemplateView):
    template_name = "academics/coordinators_academics/cd_courses_to_assemble_committee.html"
