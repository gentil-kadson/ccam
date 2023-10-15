from django.views.generic import TemplateView


class StudentHomeView(TemplateView):
    template_name = "students/home.html"


class RequestKnowledgeCertificateView(TemplateView):
    template_name = "students/knowledge_certificate_form.html"
