from django.urls import path

from ccam.people.students import views

app_name = "students"

urlpatterns = [
    path("", views.StudentHomeView.as_view(), name="home"),
    path("knowledge-certificate/", views.RequestKnowledgeCertificateView.as_view(), name="knowledge_certificate"),
]
