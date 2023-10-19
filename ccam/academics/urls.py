from django.urls import path

from ccam.academics.views import (
    CourseProgressCreateView,
    KnowledgeCertificateCreateView,
    SeacCoursesDispensalStudentDetails,
    SeacKnowledgeCertificatesStudentDetails,
    SeacViewCoursesDispensal,
    SeacViewKnowledgeCertificates,
    SubjectCourseProgressAssessView,
    SubjectKnowledgeCertificateAssessView,
    SubjectListView,
)

app_name = "academics"

urlpatterns = [
    path(
        "knowledge-certificate/create/", KnowledgeCertificateCreateView.as_view(), name="create_knowledge_certificate"
    ),
    path("course-progress/create/", CourseProgressCreateView.as_view(), name="create_course_progress"),
    path("knowledge-certificates/list", SeacViewKnowledgeCertificates.as_view(), name="knowledge_certificates"),
    path("courses-dispensal/list", SeacViewCoursesDispensal.as_view(), name="courses_dispensal"),
    path(
        "knowledge-certificates/detail/",
        SeacKnowledgeCertificatesStudentDetails.as_view(),
        name="knowledge_certificate_detail",
    ),
    path(
        "courses-dispensal/detail/",
        SeacCoursesDispensalStudentDetails.as_view(),
        name="courses_dispensal_detail",
    ),
    path("subjects/list/", SubjectListView.as_view(), name="subject_list"),
    path(
        "subjects/<int:id>/knowledge-certificate-assessments/",
        SubjectKnowledgeCertificateAssessView.as_view(),
        name="knowledge_certificate_assessments",
    ),
    path(
        "subjects/<int:id>/course-progress-assessments/",
        SubjectCourseProgressAssessView.as_view(),
        name="course_progress_assessments",
    ),
]
