from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class SeacHomeView(TemplateView):
    template_name = "seac/home.html"


class SeacViewKnowledgeCertificates(TemplateView):
    template_name = "seac/seac_view_knowledge_certificates.html"


class SeacViewCoursesDispensal(TemplateView):
    template_name = "seac/seac_view_courses_dispensal.html"


class SeacStudentDetails(TemplateView):
    template_name = "seac/student_details.html"
