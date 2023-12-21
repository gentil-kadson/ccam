from django.urls import path

from ccam.academics.students import views

urlpatterns = [
    path(
        "knowledge-certificates/create/",
        views.KnowledgeCertificateCreateView.as_view(),
        name="knowledge_certificates_create",
    ),
    path(
        "knowledge-certificates/list/",
        views.KnowledgeCertificateListView.as_view(),
        name="knowledge_certificates_list",
    ),
    path("subject-dispensals/create/", views.SubjectDispensalCreateView.as_view(), name="subject_dispensals_create"),
    path("subject-dispensals/list/", views.SubjectDispensalListView.as_view(), name="subject_dispensals_list"),
    path(
        "subject-dispensals/check-justification/<int:pk>/",
        views.SubjectDispensalApprovalCheckView.as_view(),
        name="subject_dispensal_denial_check",
    ),
    path(
        "knowledge-certificates/check-justification/<int:pk>/",
        views.KnowledgeCertificateApprovalCheckView.as_view(),
        name="knowledge_certificate_denial_check",
    ),
]
