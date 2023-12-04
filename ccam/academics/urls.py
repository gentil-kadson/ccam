from django.urls import path

from ccam.academics.views import (
    CoordinatorsCommittee,
    CoordinatorsCourseProgressComittee,
    CoordinatorsCourseProgressSubjectList,
    CoordinatorsSubjectList,
    CourseProgressCreateView,
    CourseSubjects,
    KnowledgeCertificateCreateView,
    KnowledgeCertificateListView,
    SeacCoursesDispensalStudentDetails,
    SeacKnowledgeCertificatesStudentDetails,
    SeacViewCoursesDispensal,
    SubjectCourseProgressAssessView,
    SubjectCourseProgressListView,
    SubjectCreateView,
    SubjectDeleteView,
    SubjectDetailView,
    SubjectKnowledgeCertificateAssessView,
    SubjectListView,
    SubjectUpdateView,
    TrackProcessesListView,
)

app_name = "academics"

urlpatterns = [
    path(
        "knowledge-certificate/create/", KnowledgeCertificateCreateView.as_view(), name="create_knowledge_certificate"
    ),
    path("course-progress/create/", CourseProgressCreateView.as_view(), name="create_course_progress"),
    path("knowledge-certificates/list", KnowledgeCertificateListView.as_view(), name="knowledge_certificates_list"),
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
        "coordinators/knowledge-certificates/subject/committee/",
        CoordinatorsCommittee.as_view(),
        name="kc_coordinators_committee",
    ),
    path(
        "coordinators/courses-dispensal/subject/committee/",
        CoordinatorsCourseProgressComittee.as_view(),
        name="cd_coordinators_committee",
    ),
    path(
        "coordinators/knowledge-certificates/subjects/list/",
        CoordinatorsSubjectList.as_view(),
        name="kc_coordinators_subjects_list",
    ),
    path(
        "coordinators/courses-dispensal/subjects/list/",
        CoordinatorsCourseProgressSubjectList.as_view(),
        name="cd_coordinators_subjects_list",
    ),
    path(
        "subjects/course-progress/list/", SubjectCourseProgressListView.as_view(), name="subject_course_progress_list"
    ),
    path(
        "subjects/1/knowledge-certificate-assessments/",
        SubjectKnowledgeCertificateAssessView.as_view(),
        name="knowledge_certificate_assessments",
    ),
    path(
        "subjects/1/course-progress-assessments/",
        SubjectCourseProgressAssessView.as_view(),
        name="course_progress_assessments",
    ),
    path("processes/list/", TrackProcessesListView.as_view(), name="processes_list"),
    path("course-subjects/", CourseSubjects.as_view(), name="course_subjects"),
    # Coordinator urls
    path("subjects/create/", SubjectCreateView.as_view(), name="subjects_create"),
    path("subjects/list/", SubjectListView.as_view(), name="subjects_list"),
    path("subjects/update/<int:pk>/", SubjectUpdateView.as_view(), name="subjects_update"),
    path("subjects/detail/<int:pk>/", SubjectDetailView.as_view(), name="subjects_detail"),
    path("subjects/delete/<int:pk>/", SubjectDeleteView.as_view(), name="subjects_delete"),
    # Students URLs
]
