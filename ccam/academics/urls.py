from django.urls import path

from ccam.academics.views import (
    CoordinatorsAddCourse,
    CoordinatorsCDCoursesToAssembleCommittees,
    CoordinatorsCoursesDispensalCommittees,
    CoordinatorsKCCoursesToAssembleCommittees,
    CoordinatorsKnowledgeCertificateCommittees,
    CourseProgressCreateView,
    KnowledgeCertificateCreateView,
    SeacCoursesDispensalStudentDetails,
    SeacKnowledgeCertificatesStudentDetails,
    SeacViewCoursesDispensal,
    SeacViewKnowledgeCertificates,
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
    path(
        "knowledge-certificates-committees/",
        CoordinatorsKnowledgeCertificateCommittees.as_view(),
        name="knowledge_certificate_committees",
    ),
    path(
        "courses-dispensal-committees/",
        CoordinatorsCoursesDispensalCommittees.as_view(),
        name="courses_dispensal_committees",
    ),
    path("add-course/", CoordinatorsAddCourse.as_view(), name="add_course"),
    path(
        "knowledge-certificates/courses-to-assemble-committees/",
        CoordinatorsKCCoursesToAssembleCommittees.as_view(),
        name="kc_courses_to_assemble_committee",
    ),
    path(
        "courses-dispensal/courses-to-assemble-committees/",
        CoordinatorsCDCoursesToAssembleCommittees.as_view(),
        name="cd_courses_to_assemble_committee",
    ),
]
