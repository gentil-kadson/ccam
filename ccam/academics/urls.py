from django.urls import path

from ccam.academics.coordinators.urls import urlpatterns as coordinators_urls
from ccam.academics.students.urls import urlpatterns as students_urls
from ccam.academics.teachers.urls import urlpatterns as teachers_urls
from ccam.academics.views import (
    CoordinatorsCommittee,
    CoordinatorsCourseProgressComittee,
    CoordinatorsCourseProgressSubjectList,
    CoordinatorsSubjectList,
    CourseSubjects,
    SeacCoursesDispensalUpdateView,
    SeacKnowledgeCertificateUpdateView,
    SeacSubjectDispensalListView,
    SeacKnowledgeCertificatesListView,
    SubjectCourseProgressListView,
    TrackProcessesListView,
    RejectStudentSubjectDispensalFormView,
    RejectStudentKnowledgeCertificateFormView
)

app_name = "academics"

urlpatterns = [
    path("knowledge-certificates/list", SeacKnowledgeCertificatesListView.as_view(), name="knowledge_certificates"),
    path("courses-dispensal/list", SeacSubjectDispensalListView.as_view(), name="courses_dispensal"),
    path(
        "knowledge-certificates/detail/<int:pk>/",
        SeacKnowledgeCertificateUpdateView.as_view(),
        name="knowledge_certificate_detail",
    ),
    path(
        "courses-dispensal/detail/<int:pk>",
        SeacCoursesDispensalUpdateView.as_view(),
        name="courses_dispensal_detail",
    ),
    path("knowledge-certificate-rejection/<int:pk>/", RejectStudentKnowledgeCertificateFormView.as_view(), name="reject_knowledge_certificate"),
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
    path("processes/list/", TrackProcessesListView.as_view(), name="processes_list"),
    path("course-subjects/", CourseSubjects.as_view(), name="course_subjects"),
    # Students URLs
]

urlpatterns += coordinators_urls
urlpatterns += students_urls
urlpatterns += teachers_urls
