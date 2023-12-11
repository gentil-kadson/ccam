from django.urls import path

from ccam.academics.teachers import views

urlpatterns = [
    path("teachers/<int:pk>/committees/", views.TeacherCommitteesListView.as_view(), name="teacher_committees"),
    path(
        "subjects/<int:pk>/knowledge-certificates-assessments/list/",
        views.KnowledgeCertificateGradesListView.as_view(),
        name="knowledge_certificate_assessments_list",
    ),
    path("subjects/<int:pk>/subject-dispensals-assessments/list/", views.SubjectDispensalGradesListView.as_view(), name="subject_dispensal_assessments_list"),
    path(
        "knowledge-certificate-assessments/update/<int:pk>/",
        views.KnowledgeCertificateGradesUpdateView.as_view(),
        name="knowledge_certificate_assessments_update",
    ),
    path("subject-dispensal-assessments/update/<int:pk>/", views.SubjectDispensalGradesUpdateView.as_view(), name="subject_dispensal_assessments_update")
]
