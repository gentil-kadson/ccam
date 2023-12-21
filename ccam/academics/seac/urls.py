from django.urls import path

from ccam.academics.seac import views

urlpatterns = [
    path(
        "knowledge-certificates/list", views.SeacKnowledgeCertificatesListView.as_view(), name="knowledge_certificates"
    ),
    path("courses-dispensal/list", views.SeacSubjectDispensalListView.as_view(), name="courses_dispensal"),
    path(
        "knowledge-certificates/detail/<int:pk>/",
        views.SeacKnowledgeCertificateUpdateView.as_view(),
        name="knowledge_certificate_detail",
    ),
    path(
        "courses-dispensal/detail/<int:pk>",
        views.SeacCoursesDispensalUpdateView.as_view(),
        name="courses_dispensal_detail",
    ),
    path(
        "knowledge-certificate-rejection/<int:pk>/",
        views.RejectStudentKnowledgeCertificateFormView.as_view(),
        name="reject_knowledge_certificate",
    ),
    path(
        "subject-dispensal-rejection/<int:pk>/",
        views.RejectStudentSubjectDispensalFormView.as_view(),
        name="reject_subject_dispensal",
    ),
]
