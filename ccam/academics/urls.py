from django.urls import path

from ccam.academics.views import (
    AddCourseView,
    CoordinatorsAddCourse,
    CoordinatorsCommittee,
    CoordinatorsCourseProgressComittee,
    CoordinatorsCourseProgressSubjectList,
    CoordinatorsSubjectList,
    CourseProgressCreateView,
    CourseSubjects,
    KnowledgeCertificateCreateView,
    SeacCoursesDispensalStudentDetails,
    SeacKnowledgeCertificatesStudentDetails,
    SeacViewCoursesDispensal,
    SeacViewKnowledgeCertificates,
    SubjectCourseProgressAssessView,
    SubjectCourseProgressListView,
    SubjectKnowledgeCertificateAssessView,
    SubjectListView,
    TrackProcessesListView,
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
        "coordinators/knowledge-certificates/subject/committee/",
        CoordinatorsCommittee.as_view(),
        name="kc_coordinators_committee",
    ),
    path(
        "coordinators/courses-dispensal/subject/committee/",
        CoordinatorsCourseProgressComittee.as_view(),
        name="cd_coordinators_committee",
    ),
    path("add-course/", CoordinatorsAddCourse.as_view(), name="add_course"),
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
    path("subjects/list/", SubjectListView.as_view(), name="subject_list"),
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
    path("add-courses/", AddCourseView.as_view(), name="add_courses"),
    path("processes/list/", TrackProcessesListView.as_view(), name="processes_list"),
    path("courses/<int:pk>/subjects/", CourseSubjects.as_view(), name="course-subjects"),
]
