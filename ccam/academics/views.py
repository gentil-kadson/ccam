from django.views.generic import TemplateView


class KnowledgeCertificateCreateView(TemplateView):
    template_name = "academics/knowledge_certificate_form.html"


class CourseProgressCreateView(TemplateView):
    template_name = "academics/course_progress_form.html"
