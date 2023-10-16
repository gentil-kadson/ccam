from django.urls import path

from ccam.people.seac import views

app_name = "seac"

urlpatterns = [
    path("", views.SeacHomeView.as_view(), name="home"),
    path("knowledge-certificates/", views.SeacViewKnowledgeCertificates.as_view(), name="knowledge_certificates"),
    path("courses-dispensal/", views.SeacViewCoursesDispensal.as_view(), name="courses-dispensal"),
    path("student-details/", views.SeacStudentDetails.as_view(), name="student-details"),
]
