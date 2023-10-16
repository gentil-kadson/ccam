from django.urls import path

from ccam.academics.views import KnowledgeCertificateCreateView

app_name = "academics"

urlpatterns = [
    path(
        "knowledge-certificate/create/", KnowledgeCertificateCreateView.as_view(), name="create_knowledge_certificate"
    )
]
